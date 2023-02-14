# -*- coding: utf-8 -*-
# from odoo import http


# class Kitchen(http.Controller):
#     @http.route('/kitchen/kitchen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kitchen/kitchen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kitchen.listing', {
#             'root': '/kitchen/kitchen',
#             'objects': http.request.env['kitchen.kitchen'].search([]),
#         })

#     @http.route('/kitchen/kitchen/objects/<model("kitchen.kitchen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kitchen.object', {
#             'object': obj
#         })
