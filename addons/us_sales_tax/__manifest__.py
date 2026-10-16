{
    "name": "US Sales Tax Rates",
    "version": "1.0.0",
    "summary": "Store US state sales tax rates and compute tax on an amount",
    "author": "Nelson Chen",
    "license": "LGPL-3",
    "category": "Accounting",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/us_sales_tax_views.xml",
    ],
    "installable": True,
    "application": True,
}