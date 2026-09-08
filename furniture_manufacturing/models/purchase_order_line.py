from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_brand_ids = fields.Many2many(
        related='product_id.brand_ids',
        string='Available Brands for Product'
    )

    brand_id = fields.Many2one(
        'product.brand',
        string='Brand',
        domain="[('id', 'in', product_brand_ids)]"
    )

    @api.onchange('product_id')
    def _onchange_product_id_brand(self):
        if self.brand_id and self.brand_id not in self.product_brand_ids:
            self.brand_id = False
