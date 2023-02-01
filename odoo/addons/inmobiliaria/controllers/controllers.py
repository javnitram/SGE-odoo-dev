# -*- coding: utf-8 -*-
# from odoo import http


# class Inmobiliaria(http.Controller):
#     @http.route('/inmobiliaria/inmobiliaria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inmobiliaria/inmobiliaria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inmobiliaria.listing', {
#             'root': '/inmobiliaria/inmobiliaria',
#             'objects': http.request.env['inmobiliaria.inmobiliaria'].search([]),
#         })

#     @http.route('/inmobiliaria/inmobiliaria/objects/<model("inmobiliaria.inmobiliaria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inmobiliaria.object', {
#             'object': obj
#         })
