from odoo import models, fields, api

from odoo.addons.crm.models import crm_stage
from anodoo_lead.models import crm_stage
from . import crm_stage

树状对象  class CustomerLabelCategory in customer_segment
阶段对象  class CustomerLifetimeStage in customer_lifetime
属性对象 CustomerType,  标签对象CustomerLabel, 日志对象CustomerAllot

#继承
class Customer(models.Model):	
    _inherit = 'res.partner'

#新简单对象
class Customer(models.Model):
	_name = ''
	_description = ''
	_rec_name = 'name'
    _order = 'id'
	
    
    name = fields.Char('名称', required=True)
    
    sequence = fields.Integer('序号', default=10)
    
    description = fields.Text('描述')
    
    #其他常用字段
    active = fields.Boolean('激活', default=True)
    
    customer_identity = fields.Char('唯一标识信息', help='客户唯一标识信息')
    
    is_default = fields.Boolean('是否默认', default=False)
    
    customer_id = fields.Many2one('res.partner', string='客户1', help='客户与客户的关系的主方')
    
    manage_user_id = fields.Many2one('res.users', string='管理员')
    
    fold = fields.Boolean('合并', default=False)
    
    customer_type = fields.Selection([('company', '公司客户'), ('person', '个人客户'), ('family', '家庭客户')], 
                           string='客户性质', default='company', help='客户类型定义，可扩展')
                           
   	customer_priority = fields.Selection([('0', 'Low'),  ('1', 'Medium'),  ('2', 'High'), ('3', 'Very High')], 
   	string='优先级', index=True, default='0')
       
    resume_line_ids = fields.One2many(related='employee_id.resume_line_ids', readonly=False)
       
    @api.model
    def default_get(self, fields):
        ctx = dict(self.env.context)
        if ctx.get('default_team_id') and not ctx.get('crm_team_mono'):
            ctx.pop('default_team_id')
        return super(Stage, self.with_context(ctx)).default_get(fields)
    
    @api.model
    def default_get(self, fields):
        vals = super(AccountBankStmtCashWizard, self).default_get(fields)
        balance = self.env.context.get('balance')
        statement_id = self.env.context.get('statement_id')
        if 'start_bank_stmt_ids' in fields and not vals.get('start_bank_stmt_ids') and statement_id and balance == 'start':
            vals['start_bank_stmt_ids'] = [(6, 0, [statement_id])]
        if 'end_bank_stmt_ids' in fields and not vals.get('end_bank_stmt_ids') and statement_id and balance == 'close':
            vals['end_bank_stmt_ids'] = [(6, 0, [statement_id])]

        return vals
    
    @api.depends('cashbox_lines_ids', 'cashbox_lines_ids.coin_value', 'cashbox_lines_ids.number')
    def _compute_total(self):
        for cashbox in self:
            cashbox.total = sum([line.subtotal for line in cashbox.cashbox_lines_ids])
            #stage.team_count = self.env['crm.team'].search_count([])
            
    @api.model_create_multi
    def create(self, vals):
        cashboxes = super(AccountBankStmtCashWizard, self).create(vals)
        cashboxes._validate_cashbox()
        return cashboxes

    def write(self, vals):
        res = super(AccountBankStmtCashWizard, self).write(vals)
        self._validate_cashbox()
        return res
    
    @api.depends('attribute_line_ids.active', 'attribute_line_ids.product_tmpl_id')
    def _compute_products(self):
        for pa in self:
            pa.product_tmpl_ids = pa.attribute_line_ids.product_tmpl_id
    
    
    _cr = property(lambda self: self.env.cr)
    _uid = property(lambda self: self.env.uid)
    _context = property(lambda self: self.env.context)
self.env['account.journal'].browse

program = self.env['sale.coupon.program'].browse(self.env.context.get('active_id'))

        vals = {'program_id': program.id}

for count in range(0, self.nbr_coupons):

for partner in self.env['res.partner'].search(safe_eval(self.partners_domain)):
	vals.update({'partner_id': partner.id})

subject = '%s, a coupon has been generated for you' % (partner.name)

template = self.env.ref('sale_coupon.mail_template_sale_coupon', raise_if_not_found=False)

template.send_mail(coupon.id, email_values={'email_to': partner.email, 'email_from': self.env.user.email or '', 'subject': subject,})

getattr(self, field)



     
