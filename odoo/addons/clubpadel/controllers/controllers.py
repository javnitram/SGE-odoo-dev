# -*- coding: utf-8 -*-
# from odoo import http


# class Clubpadel(http.Controller):
#     @http.route('/clubpadel/clubpadel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clubpadel/clubpadel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clubpadel.listing', {
#             'root': '/clubpadel/clubpadel',
#             'objects': http.request.env['clubpadel.clubpadel'].search([]),
#         })

#     @http.route('/clubpadel/clubpadel/objects/<model("clubpadel.clubpadel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clubpadel.object', {
#             'object': obj
#         })
