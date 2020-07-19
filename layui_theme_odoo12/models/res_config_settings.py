# !user/bin/env python3
# -*- coding: utf-8 -*-
# Author: Artorias
import os
import base64

from odoo import models, fields

BASE_PATH = os.path.dirname(os.path.dirname(__file__))


class LayuiThemeConfig(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'layui_theme_odoo12.config'

    title = fields.Char('登录页标题', default_model='layui_theme_odoo12.config')
    english_title = fields.Char('登录页英文标题', default_model='layui_theme_odoo12.config')
    logo = fields.Binary('logo大图', default_model='layui_theme_odoo12.config')
    logo_mini = fields.Binary('logo小图', default_model='layui_theme_odoo12.config')

    @staticmethod
    def _get_logo(logo_type):
        file = 'logo.png' if logo_type == 'normal' else 'logo_mini.png'
        path = os.path.join(BASE_PATH, 'static', 'imgs', file)
        with open(path, 'rb') as f:
            content = base64.b64encode((f.read()))
        return content

    def set_values(self):
        self.env['ir.config_parameter'] \
            .set_param('layui_theme_odoo12_title', (self.title or '').strip())
        self.env['ir.config_parameter'] \
            .set_param('layui_theme_odoo12_english_title', (self.english_title or '').strip())
        self.env['ir.config_parameter'] \
            .set_param('layui_theme_odoo12_logo', self.logo)
        self.env['ir.config_parameter'] \
            .set_param('layui_theme_odoo12_logo_mini', self.logo_mini)

    def get_values(self):
        title = self.env['ir.config_parameter'] \
            .get_param('layui_theme_odoo12_title', default='富能通产品开发平台')
        english_title = self.env['ir.config_parameter'] \
            .get_param('layui_theme_odoo12_english_title', default='Funenc Dev Framework')
        logo = self.env['ir.config_parameter'] \
            .get_param('layui_theme_odoo12_logo', default=self._get_logo('normal'))
        logo_mini = self.env['ir.config_parameter'] \
            .get_param('layui_theme_odoo12_logo_mini', default=self._get_logo('mini'))
        return dict(title=title, english_title=english_title, logo=logo, logo_mini=logo_mini)
