# -*- coding: utf-8 -*-
# from odoo import http


# class Tallerbmx(http.Controller):
#     @http.route('/tallerbmx/tallerbmx', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tallerbmx/tallerbmx/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tallerbmx.listing', {
#             'root': '/tallerbmx/tallerbmx',
#             'objects': http.request.env['tallerbmx.tallerbmx'].search([]),
#         })

#     @http.route('/tallerbmx/tallerbmx/objects/<model("tallerbmx.tallerbmx"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tallerbmx.object', {
#             'object': obj
#         })
