# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/hospital(http.Controller):
#     @http.route('//mnt/extra-addons/hospital//mnt/extra-addons/hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/hospital//mnt/extra-addons/hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/hospital.listing', {
#             'root': '//mnt/extra-addons/hospital//mnt/extra-addons/hospital',
#             'objects': http.request.env['/mnt/extra-addons/hospital./mnt/extra-addons/hospital'].search([]),
#         })

#     @http.route('//mnt/extra-addons/hospital//mnt/extra-addons/hospital/objects/<model("/mnt/extra-addons/hospital./mnt/extra-addons/hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/hospital.object', {
#             'object': obj
#         })
