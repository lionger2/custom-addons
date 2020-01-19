'''
Created on Jan 10, 2020

@author: lionger
'''
from odoo import api, fields, models

class IrModel(models.Model):    
    _inherit = 'ir.model'
    
    def_module = fields.Many2one('ir.module.module', compute='_in_def_module', string='定义模块', store=True,  help='the module in which the object is defined')
    
    @api.depends()
    def _in_def_module(self):
        for record in self:
            domain = [('model', '=', 'ir.model'), ('res_id', '=', record.id)]
            rec = self.env['ir.model.data'].sudo().search(domain, limit=1, order='id')
            name = rec[0].module
            
            rec = self.env['ir.module.module'].sudo().search([('name', '=', name)])
            record.def_module = rec[0]
            