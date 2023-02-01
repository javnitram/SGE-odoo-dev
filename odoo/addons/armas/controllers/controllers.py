# -*- coding: utf-8 -*-
# from odoo import http


# class Armas(http.Controller):
#     @http.route('/armas/armas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/armas/armas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('armas.listing', {
#             'root': '/armas/armas',
#             'objects': http.request.env['armas.armas'].search([]),
#         })

#     @http.route('/armas/armas/objects/<model("armas.armas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('armas.object', {
#             'object': obj
#         })
