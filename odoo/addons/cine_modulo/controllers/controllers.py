# -*- coding: utf-8 -*-
# from odoo import http


# class CineModulo(http.Controller):
#     @http.route('/cine_modulo/cine_modulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cine_modulo/cine_modulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cine_modulo.listing', {
#             'root': '/cine_modulo/cine_modulo',
#             'objects': http.request.env['cine_modulo.cine_modulo'].search([]),
#         })

#     @http.route('/cine_modulo/cine_modulo/objects/<model("cine_modulo.cine_modulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cine_modulo.object', {
#             'object': obj
#         })
