# -*- coding: utf-8 -*-
# from odoo import http


# class Libreria(http.Controller):
#     @http.route('/libreria/libreria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria/libreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria.listing', {
#             'root': '/libreria/libreria',
#             'objects': http.request.env['libreria.libreria'].search([]),
#         })

#     @http.route('/libreria/libreria/objects/<model("libreria.libreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria.object', {
#             'object': obj
#         })
