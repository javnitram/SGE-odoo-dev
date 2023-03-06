# -*- coding: utf-8 -*-
# from odoo import http


# class Taberna(http.Controller):
#     @http.route('/taberna/taberna', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taberna/taberna/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taberna.listing', {
#             'root': '/taberna/taberna',
#             'objects': http.request.env['taberna.taberna'].search([]),
#         })

#     @http.route('/taberna/taberna/objects/<model("taberna.taberna"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taberna.object', {
#             'object': obj
#         })
