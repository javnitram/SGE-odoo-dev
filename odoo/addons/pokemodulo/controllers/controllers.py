# -*- coding: utf-8 -*-
# from odoo import http


# class Pokemodulo(http.Controller):
#     @http.route('/pokemodulo/pokemodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pokemodulo/pokemodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pokemodulo.listing', {
#             'root': '/pokemodulo/pokemodulo',
#             'objects': http.request.env['pokemodulo.pokemodulo'].search([]),
#         })

#     @http.route('/pokemodulo/pokemodulo/objects/<model("pokemodulo.pokemodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pokemodulo.object', {
#             'object': obj
#         })
