# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class siwei_dev(models.Model):
#     _name = 'siwei_dev.siwei_dev'
#     _description = 'siwei_dev.siwei_dev'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
