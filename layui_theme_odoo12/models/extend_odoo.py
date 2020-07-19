# !user/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artorias
import os
import logging

from odoo.exceptions import MissingError
from odoo.fields import Many2many, One2many
from odoo import tools, api
from odoo.tools import view_validation
from odoo.tools.convert import xml_import
from odoo.tools.view_validation import validate
from odoo.models import BaseModel

from lxml import etree

_logger = logging.getLogger(__name__)


# 改写解析xml的方法，读取其中的icon值
def _tag_menuitem(self, rec, data_node=None, mode=None):
    rec_id = rec.get("id")
    self._test_xml_id(rec_id)

    # The parent attribute was specified, if non-empty determine its ID, otherwise
    # explicitly make a top-level menu
    if rec.get('parent'):
        menu_parent_id = self.id_get(rec.get('parent', ''))
    else:
        # we get here with <menuitem parent="">, explicit clear of parent, or
        # if no parent attribute at all but menu name is not a menu path
        menu_parent_id = False
    values = {'parent_id': menu_parent_id}
    if rec.get('name'):
        values['name'] = rec.get('name')
    try:
        res = [self.id_get(rec.get('id', ''))]
    except:
        res = None

    if rec.get('action'):
        a_action = rec.get('action')

        # determine the type of action
        action_model, action_id = self.model_id_get(a_action)
        action_type = action_model.split('.')[-1]  # keep only type part
        values['action'] = "ir.actions.%s,%d" % (action_type, action_id)

        if not values.get('name') and action_type in ('act_window', 'wizard', 'url', 'client', 'server'):
            resw = self.env[action_model].sudo().browse(action_id).name
            if resw:
                values['name'] = resw

    if not values.get('name'):
        # ensure menu has a name
        values['name'] = rec_id or '?'

    if rec.get('sequence'):
        values['sequence'] = int(rec.get('sequence'))

    values['active'] = self.nodeattr2bool(rec, 'active', default=True)

    if rec.get('groups'):
        g_names = rec.get('groups', '').split(',')
        groups_value = []
        for group in g_names:
            if group.startswith('-'):
                group_id = self.id_get(group[1:])
                groups_value.append((3, group_id))
            else:
                group_id = self.id_get(group)
                groups_value.append((4, group_id))
        values['groups_id'] = groups_value

    if not values.get('parent_id'):
        if rec.get('web_icon'):
            values['web_icon'] = rec.get('web_icon')
    # 读取是否有icon
    if rec.get('icon'):
        values['icon'] = rec.get('icon')
    xid = self.make_xml_id(rec_id)
    data = dict(xml_id=xid, values=values, noupdate=self.isnoupdate(data_node))
    self.env['ir.ui.menu']._load_records([data], self.mode == 'update')


# 变更xml属性解析路径
def relaxng(view_type):
    """ Return a validator for the given view type, or None. """
    cur_path, _ = os.path.split(os.path.realpath(__file__))
    if view_type not in view_validation._relaxng_cache:
        with tools.file_open(os.path.join(cur_path, '..', 'rng', '%s_view.rng' % view_type)) as frng:
            try:
                relaxng_doc = etree.parse(frng)
                view_validation._relaxng_cache[view_type] = etree.RelaxNG(relaxng_doc)
            except Exception:
                _logger.exception('Failed to load RelaxNG XML schema for views validation')
                view_validation._relaxng_cache[view_type] = None
    return view_validation._relaxng_cache[view_type]


xml_import._tag_menuitem = _tag_menuitem
view_validation.relaxng = relaxng

# 先在list里删除原有的tree验证，然后利用validate装饰器再添加自定的验证
for index, pred in enumerate(view_validation._validators['tree']):
    if pred.__name__ == 'valid_field_in_tree':
        view_validation._validators['tree'].pop(index)
        break


@validate('tree')
def valid_field_in_tree(arch):
    """ Children of ``tree`` view must be ``field`` or ``button``."""
    return all(
        child.tag in ('field', 'button', 'widget')
        for child in arch.xpath('/tree/*')
    )


def get_last_record(self):
    '''
    model结果中查找最后一条数据
    :param self:
    :return:
    '''
    if len(self) == 0:
        return self
    else:
        return self[-1]


def get_first_record(self):
    '''
    model结果中查找第一条数据
    :param self:
    :return:
    '''
    if len(self) == 0:
        return self
    else:
        return self[0]



def read_no_ids(self, fields=None, load='_classic_read'):
    # 扩展方法，读取时将字段内one2many, many2many的字段读出为[{'id': 1}, {'name': 'admin'}...]，而不是[1, 3, 5...]这种ids
    # check access rights
    self.check_access_rights('read')
    fields = self.check_field_access_rights('read', fields)

    # split fields into stored and computed fields
    stored, inherited, computed = [], [], []
    for name in fields:
        field = self._fields.get(name)
        if field:
            if field.store:
                stored.append(name)
            elif field.base_field.store:
                inherited.append(name)
            else:
                computed.append(name)
        else:
            _logger.warning("%s.read() with unknown field '%s'", self._name, name)

    # fetch stored fields from the database to the cache; this should feed
    # the prefetching of secondary records
    self._read_from_database(stored, inherited)

    # retrieve results from records; this takes values from the cache and
    # computes remaining fields
    result = []
    name_fields = [(name, self._fields[name]) for name in (stored + inherited + computed)]
    use_name_get = (load == '_classic_read')
    for record in self:
        try:
            values = {'id': record.id}
            for name, field in name_fields:
                # many2many或者one2many时读出所有值
                if isinstance(field, Many2many) is True or isinstance(field, One2many):
                    ids_value = []
                    for r in record[name]:
                        _fields = [(_name, r._fields[_name]) for _name in r._fields]
                        for _name, _field in _fields:
                            child_value = _field.convert_to_read(r[_name], r, use_name_get)
                            ids_value.append({_name: child_value})
                    values[name] = ids_value
                else:
                    values[name] = field.convert_to_read(record[name], record, use_name_get)
            result.append(values)
        except MissingError:
            pass

    return result


BaseModel.last, BaseModel.first, BaseModel.read_no_ids = get_last_record, get_last_record, read_no_ids
