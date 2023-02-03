# -*- coding: utf-8 -*-
# from odoo import http


# class Ricardohl(http.Controller):
#     @http.route('/ricardohl/ricardohl', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ricardohl/ricardohl/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ricardohl.listing', {
#             'root': '/ricardohl/ricardohl',
#             'objects': http.request.env['ricardohl.ricardohl'].search([]),
#         })

#     @http.route('/ricardohl/ricardohl/objects/<model("ricardohl.ricardohl"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ricardohl.object', {
#             'object': obj
#         })
