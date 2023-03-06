# -*- coding: utf-8 -*-
# from odoo import http


# class Musica(http.Controller):
#     @http.route('/musica/musica', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/musica/musica/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('musica.listing', {
#             'root': '/musica/musica',
#             'objects': http.request.env['musica.musica'].search([]),
#         })

#     @http.route('/musica/musica/objects/<model("musica.musica"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('musica.object', {
#             'object': obj
#         })
