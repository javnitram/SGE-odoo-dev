# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloIntento(http.Controller):
#     @http.route('/modulo_intento/modulo_intento', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_intento/modulo_intento/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_intento.listing', {
#             'root': '/modulo_intento/modulo_intento',
#             'objects': http.request.env['modulo_intento.modulo_intento'].search([]),
#         })

#     @http.route('/modulo_intento/modulo_intento/objects/<model("modulo_intento.modulo_intento"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_intento.object', {
#             'object': obj
#         })
