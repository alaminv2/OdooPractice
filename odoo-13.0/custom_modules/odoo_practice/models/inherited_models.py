from odoo import api, fields, models

class saleOrderInherit(models.Model):
    _inherit = 'sale.order'

    demo_name = fields.Char(string = 'Demo Add')