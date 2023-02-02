# -*- coding: utf-8 -*-
# from odoo import http


# class Ooddle(http.Controller):
#     @http.route('/ooddle/ooddle', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ooddle/ooddle/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ooddle.listing', {
#             'root': '/ooddle/ooddle',
#             'objects': http.request.env['ooddle.ooddle'].search([]),
#         })

#     @http.route('/ooddle/ooddle/objects/<model("ooddle.ooddle"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ooddle.object', {
#             'object': obj
#         })
