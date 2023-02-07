# -*- coding: utf-8 -*-
# from odoo import http


# class Gatoteca(http.Controller):
#     @http.route('/gatoteca/gatoteca', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gatoteca/gatoteca/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gatoteca.listing', {
#             'root': '/gatoteca/gatoteca',
#             'objects': http.request.env['gatoteca.gatoteca'].search([]),
#         })

#     @http.route('/gatoteca/gatoteca/objects/<model("gatoteca.gatoteca"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gatoteca.object', {
#             'object': obj
#         })
