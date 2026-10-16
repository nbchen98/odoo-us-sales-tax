from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestUsSalesTax(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.california = cls.env["res.country.state"].search(
            [("country_id.code", "=", "US"), ("code", "=", "CA")], limit=1
        )
        cls.tax = cls.env["us.sales.tax"].create(
            {"state_id": cls.california.id, "rate": 7.25}
        )

    def test_compute_tax(self):
        self.assertEqual(self.tax.compute_tax(100), 7.25)
        self.assertEqual(self.tax.compute_tax(19.99), 1.45)

    def test_rate_out_of_range_is_rejected(self):
        with self.assertRaises(ValidationError):
            self.env["us.sales.tax"].create(
                {"state_id": self.california.id, "rate": 50}
            )