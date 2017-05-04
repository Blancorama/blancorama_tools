# -*- coding: utf-8 -*-

from openerp import models, fields, api

class product_product(models.Model):
	_inherit = 'product.product'
	
	measurements = fields.Char()
	brand = fields.Char()
	composition = fields.Char()
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class sale_order(models.Model):
    _inherit = 'sale.order'

    billing_required = fields.Boolean(default=True)

    def compute_total(self,amount_total):
        return amount_total + amount_total * 0.07
    
    def compute_subtotal(self,quantity,price_unit):
        return quantity * price_unit + quantity * price_unit * 0.07
           
    def compute_product_price_unit(self,price_unit):
        return price_unit + price_unit * 0.07

# class product_product(models.Model):
# 	_inherit = 'sale.order'

# 	@api.multi
# 	def action_quotation_send(self):
# 		'''
# 		This function opens a window to compose an email, with the edi sale template message loaded by default
# 		'''
# 		self.ensure_one()
# 		ir_model_data = self.env['ir.model.data']
# 		try:
# 			print "pasa Here"
# 			template_id = ir_model_data.get_object_reference('blancorama_product', 'email_template_edi_sale_modified')[0]
# 			print "no pasa here"
# 		except ValueError,e:
# 			print "Error"
# 			print str(e)
# 			template_id = False
# 		try:
# 			compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
# 		except ValueError:
# 			compose_form_id = False
		
# 		print template_id
# 		print compose_form_id

# 		ctx = dict()
# 		ctx.update({
# 			'default_model': 'sale.order',
# 			'default_res_id': self.ids[0],
# 			'default_use_template': bool(template_id),
# 			'default_template_id': template_id,
# 			'default_composition_mode': 'comment',
# 			'mark_so_as_sent': True
# 		})
# 		return {
# 			'type': 'ir.actions.act_window',
# 			'view_type': 'form',
# 			'view_mode': 'form',
# 			'res_model': 'mail.compose.message',
# 			'views': [(compose_form_id, 'form')],
# 			'view_id': compose_form_id,
# 			'target': 'new',
# 			'context': ctx,
# 		}
