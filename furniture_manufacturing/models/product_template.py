from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_ids = fields.Many2many(
        'product.brand',
        string='Available Brands',
        help='Select the brands that are available for this product.'
    )
