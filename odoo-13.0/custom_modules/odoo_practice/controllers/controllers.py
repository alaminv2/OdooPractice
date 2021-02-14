# -*- coding: utf-8 -*-
# from odoo import http


# class OdooPractice(http.Controller):
#     @http.route('/odoo_practice/odoo_practice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_practice/odoo_practice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_practice.listing', {
#             'root': '/odoo_practice/odoo_practice',
#             'objects': http.request.env['odoo_practice.odoo_practice'].search([]),
#         })

#     @http.route('/odoo_practice/odoo_practice/objects/<model("odoo_practice.odoo_practice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_practice.object', {
#             'object': obj
#         })
