# -*- coding: utf-8 -*-
# from odoo import http


# class CmVeterinaria(http.Controller):
#     @http.route('/cm_veterinaria/cm_veterinaria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cm_veterinaria/cm_veterinaria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cm_veterinaria.listing', {
#             'root': '/cm_veterinaria/cm_veterinaria',
#             'objects': http.request.env['cm_veterinaria.cm_veterinaria'].search([]),
#         })

#     @http.route('/cm_veterinaria/cm_veterinaria/objects/<model("cm_veterinaria.cm_veterinaria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cm_veterinaria.object', {
#             'object': obj
#         })
