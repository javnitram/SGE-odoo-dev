# -*- coding: utf-8 -*-
# from odoo import http


# class Taller(http.Controller):
#     @http.route('/taller/taller', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taller/taller/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taller.listing', {
#             'root': '/taller/taller',
#             'objects': http.request.env['taller.taller'].search([]),
#         })

#     @http.route('/taller/taller/objects/<model("taller.taller"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taller.object', {
#             'object': obj
#         })
