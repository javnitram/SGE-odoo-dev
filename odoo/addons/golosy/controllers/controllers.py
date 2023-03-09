# -*- coding: utf-8 -*-
# from odoo import http


# class Golosy(http.Controller):
#     @http.route('/golosy/golosy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/golosy/golosy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('golosy.listing', {
#             'root': '/golosy/golosy',
#             'objects': http.request.env['golosy.golosy'].search([]),
#         })

#     @http.route('/golosy/golosy/objects/<model("golosy.golosy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('golosy.object', {
#             'object': obj
#         })
