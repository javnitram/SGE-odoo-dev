# -*- coding: utf-8 -*-
# from odoo import http


# class Gimnasio(http.Controller):
#     @http.route('/gimnasio/gimnasio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gimnasio/gimnasio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gimnasio.listing', {
#             'root': '/gimnasio/gimnasio',
#             'objects': http.request.env['gimnasio.gimnasio'].search([]),
#         })

#     @http.route('/gimnasio/gimnasio/objects/<model("gimnasio.gimnasio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gimnasio.object', {
#             'object': obj
#         })
