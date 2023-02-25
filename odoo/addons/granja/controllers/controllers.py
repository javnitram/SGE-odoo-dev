# -*- coding: utf-8 -*-
# from odoo import http


# class Granja(http.Controller):
#     @http.route('/granja/granja', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/granja/granja/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('granja.listing', {
#             'root': '/granja/granja',
#             'objects': http.request.env['granja.granja'].search([]),
#         })

#     @http.route('/granja/granja/objects/<model("granja.granja"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('granja.object', {
#             'object': obj
#         })
