from odoo import api, fields, models
from odoo.exceptions import ValidationError


class UsSalesTax(models.Model):
    _name = "us.sales.tax"
    _description = "US State Sales Tax Rate"
    _rec_name = "state_id"
    _order = "state_id"

    state_id = fields.Many2one(
        "res.country.state",
        string="State",
        required=True,
        domain="[('country_id.code', '=', 'US')]",
    )
    rate = fields.Float(string="Rate (%)", digits=(5, 3), required=True)
    active = fields.Boolean(default=True)

    @api.constrains("rate")
    def _check_rate(self):
        for record in self:
            if not 0 <= record.rate <= 20:
                raise ValidationError("Sales tax rate must be between 0% and 20%.")

    def compute_tax(self, amount):
        """Return the sales tax on `amount`, rounded to cents."""
        self.ensure_one()
        return round(amount * self.rate / 100, 2)