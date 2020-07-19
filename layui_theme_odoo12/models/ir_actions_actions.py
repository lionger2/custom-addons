# !user/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artorias
from odoo import models, fields, api


class LayuiThemeIrActionsActions(models.Model):
    _inherit = 'ir.actions.actions'

    bind_tree_buttons = fields.Text()

    @api.model
    def get_action_id(self, bind_tree_buttons):
        button_list = []
        for action in bind_tree_buttons:
            action_ref = self.env.ref(action.strip())
            button_list.append({
                'name': action_ref.name,
                'id': action_ref.id
            })
        return button_list
