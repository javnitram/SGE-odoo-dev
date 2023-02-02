# -*- coding: utf-8 -*-
# from odoo import http


# class Pruebas(http.Controller):
#     @http.route('/pruebas/pruebas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pruebas/pruebas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pruebas.listing', {
#             'root': '/pruebas/pruebas',
#             'objects': http.request.env['pruebas.pruebas'].search([]),
#         })

#     @http.route('/pruebas/pruebas/objects/<model("pruebas.pruebas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pruebas.object', {
#             'object': obj
#         })
