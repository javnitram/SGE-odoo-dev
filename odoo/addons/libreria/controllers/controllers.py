# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/libreria(http.Controller):
#     @http.route('//mnt/extra-addons/libreria//mnt/extra-addons/libreria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/libreria//mnt/extra-addons/libreria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/libreria.listing', {
#             'root': '//mnt/extra-addons/libreria//mnt/extra-addons/libreria',
#             'objects': http.request.env['/mnt/extra-addons/libreria./mnt/extra-addons/libreria'].search([]),
#         })

#     @http.route('//mnt/extra-addons/libreria//mnt/extra-addons/libreria/objects/<model("/mnt/extra-addons/libreria./mnt/extra-addons/libreria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/libreria.object', {
#             'object': obj
#         })
