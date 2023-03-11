# -*- coding: utf-8 -*-
# from odoo import http


# class Concesionario(http.Controller):
#     @http.route('/concesionario/concesionario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/concesionario/concesionario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('concesionario.listing', {
#             'root': '/concesionario/concesionario',
#             'objects': http.request.env['concesionario.concesionario'].search([]),
#         })

#     @http.route('/concesionario/concesionario/objects/<model("concesionario.concesionario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('concesionario.object', {
#             'object': obj
#         })
