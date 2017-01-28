# -*- coding: utf-8 -*-
from openerp import http

# class BlancoramaProduct(http.Controller):
#     @http.route('/blancorama_product/blancorama_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blancorama_product/blancorama_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blancorama_product.listing', {
#             'root': '/blancorama_product/blancorama_product',
#             'objects': http.request.env['blancorama_product.blancorama_product'].search([]),
#         })

#     @http.route('/blancorama_product/blancorama_product/objects/<model("blancorama_product.blancorama_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blancorama_product.object', {
#             'object': obj
#         })