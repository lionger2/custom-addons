# !user/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artorias
import operator

from odoo import api, fields, models, tools


class LayuiThemeMenu(models.Model):
    '''
    继承ir.ui.menu创建图标字段，并返回图标字段信息
    '''
    _inherit = 'ir.ui.menu'

    icon = fields.Char(string='图标')

    @api.model
    @tools.ormcache_context('self._uid', keys=('lang',))
    def load_menus_root(self):
        # 添加icon字段
        fields = ['name', 'sequence', 'parent_id', 'action', 'web_icon_data', 'icon']
        menu_roots = self.get_user_roots()
        menu_roots_data = menu_roots.read(fields) if menu_roots else []
        menu_root = {
            'id': False,
            'name': 'root',
            'parent_id': [-1, ''],
            'children': menu_roots_data,
            'all_menu_ids': menu_roots.ids,
        }
        menu_roots._set_menuitems_xmlids(menu_root)
        return menu_root

    @api.model
    @tools.ormcache_context('self._uid', 'debug', keys=('lang',))
    def load_menus(self, debug):
        """ Loads all menu items (all applications and their sub-menus).

        :return: the menu root
        :rtype: dict('children': menu_nodes)
        """
        # 添加icon字段
        fields = ['name', 'sequence', 'parent_id', 'action', 'web_icon', 'web_icon_data', 'icon']
        menu_roots = self.get_user_roots()
        menu_roots_data = menu_roots.read(fields) if menu_roots else []
        menu_root = {
            'id': False,
            'name': 'root',
            'parent_id': [-1, ''],
            'children': menu_roots_data,
            'all_menu_ids': menu_roots.ids,
        }
        if not menu_roots_data:
            return menu_root
        menus = self.search([('id', 'child_of', menu_roots.ids)])
        menu_items = menus.read(fields)
        menu_items.extend(menu_roots_data)
        menu_root['all_menu_ids'] = menus.ids  # includes menu_roots!
        menu_items_map = {menu_item["id"]: menu_item for menu_item in menu_items}
        for menu_item in menu_items:
            parent = menu_item['parent_id'] and menu_item['parent_id'][0]
            if parent in menu_items_map:
                menu_items_map[parent].setdefault(
                    'children', []).append(menu_item)
        for menu_item in menu_items:
            menu_item.setdefault('children', []).sort(key=operator.itemgetter('sequence'))
        (menu_roots + menus)._set_menuitems_xmlids(menu_root)
        return menu_root