# -*- coding: utf-8 -*-
# © 2016 Jarsa Sistemas, S.A. de C.V.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Payment Conekta",
    "summary": "Payment Acquirer: Conekta Implementation",
    "version": "9.0.1.0.0",
    "category": "Hidden",
    "website": "https://www.jarsa.com.mx/",
    "author": "JARSA Sistemas, S.A. de C.V.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": ["conekta"],
    },
    "depends": [
        "payment",
        "website_sale",
    ],
    "data": [
        "security/security.xml",
        "views/conekta.xml",
        "views/payment_acquirer_view.xml",
        "data/payment_acquirer_data.xml",
        "views/assets_frontend.xml",
        "wizards/conekta_refund_wizard_view.xml",
        "views/sale_order_view.xml",
    ],
    "demo": [
        "demo/payment_acquirer_demo.xml",
    ]
}
