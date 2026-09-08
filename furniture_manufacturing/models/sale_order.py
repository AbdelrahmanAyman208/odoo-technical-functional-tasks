from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_website_order = fields.Boolean(
        string='Website Order',
        help="Indicates if this order was placed through the website.",
        readonly=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'website_id' in vals and vals.get('website_id'):
                vals['is_website_order'] = True
        return super().create(vals_list)
