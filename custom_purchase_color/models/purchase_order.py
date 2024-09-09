from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    color_id = fields.Many2one('product.attribute.value', string="Color", domain="[('attribute_id.name', '=', 'Color')]")
    size_id = fields.Many2one('product.attribute.value', string="Size", domain="[('attribute_id.name', '=', 'Size')]")
    invoice_count = fields.Integer(string="Invoice Count")
    sku = fields.Char(string="SKU", related='product_id.default_code', readonly=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            # Reset color and size fields when the product changes
            self.color_id = False
            self.size_id = False
