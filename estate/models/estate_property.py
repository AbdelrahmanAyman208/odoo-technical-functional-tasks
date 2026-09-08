from odoo import models,fields,api

class EstateProperty(models.Model):
    _name = "estate.property" # In Database name will be "estate_property"
    _description = "Estate Properties"

    name = fields.Char(required=True)
    description = fields.Text()
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    has_garden = fields.Boolean()
    garden_area = fields.Integer()

    total_area = fields.Integer(compute="_compute_total_area")

    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    

