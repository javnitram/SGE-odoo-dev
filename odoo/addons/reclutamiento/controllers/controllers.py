# -*- coding: utf-8 -*-
# from odoo import http


# class Reclutamiento(http.Controller):
#     @http.route('/reclutamiento/reclutamiento', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reclutamiento/reclutamiento/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reclutamiento.listing', {
#             'root': '/reclutamiento/reclutamiento',
#             'objects': http.request.env['reclutamiento.reclutamiento'].search([]),
#         })

#     @http.route('/reclutamiento/reclutamiento/objects/<model("reclutamiento.reclutamiento"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reclutamiento.object', {
#             'object': obj
#         })
