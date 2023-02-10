# -*- coding: utf-8 -*-
# from odoo import http


# class Payasos(http.Controller):
#     @http.route('/payasos/payasos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/payasos/payasos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('payasos.listing', {
#             'root': '/payasos/payasos',
#             'objects': http.request.env['payasos.payasos'].search([]),
#         })

#     @http.route('/payasos/payasos/objects/<model("payasos.payasos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('payasos.object', {
#             'object': obj
#         })
