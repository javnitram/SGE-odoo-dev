# -*- coding: utf-8 -*-
# from odoo import http


# class Floristeria(http.Controller):
#     @http.route('/floristeria/floristeria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/floristeria/floristeria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('floristeria.listing', {
#             'root': '/floristeria/floristeria',
#             'objects': http.request.env['floristeria.floristeria'].search([]),
#         })

#     @http.route('/floristeria/floristeria/objects/<model("floristeria.floristeria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('floristeria.object', {
#             'object': obj
#         })
