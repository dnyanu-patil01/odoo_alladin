from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    variant_id = fields.Many2one('product.template.attribute.value', string='Variant')
