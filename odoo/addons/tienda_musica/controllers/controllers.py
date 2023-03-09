# -*- coding: utf-8 -*-
# from odoo import http


# class TiendaMusica(http.Controller):
#     @http.route('/tienda_musica/tienda_musica', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tienda_musica/tienda_musica/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tienda_musica.listing', {
#             'root': '/tienda_musica/tienda_musica',
#             'objects': http.request.env['tienda_musica.tienda_musica'].search([]),
#         })

#     @http.route('/tienda_musica/tienda_musica/objects/<model("tienda_musica.tienda_musica"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tienda_musica.object', {
#             'object': obj
#         })
