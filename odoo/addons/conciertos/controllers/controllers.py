# -*- coding: utf-8 -*-
# from odoo import http


# class Conciertos(http.Controller):
#     @http.route('/conciertos/conciertos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/conciertos/conciertos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('conciertos.listing', {
#             'root': '/conciertos/conciertos',
#             'objects': http.request.env['conciertos.conciertos'].search([]),
#         })

#     @http.route('/conciertos/conciertos/objects/<model("conciertos.conciertos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('conciertos.object', {
#             'object': obj
#         })
