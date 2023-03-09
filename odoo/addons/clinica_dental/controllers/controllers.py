# -*- coding: utf-8 -*-
# from odoo import http


# class ClinicaDental(http.Controller):
#     @http.route('/clinica_dental/clinica_dental', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinica_dental/clinica_dental/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinica_dental.listing', {
#             'root': '/clinica_dental/clinica_dental',
#             'objects': http.request.env['clinica_dental.clinica_dental'].search([]),
#         })

#     @http.route('/clinica_dental/clinica_dental/objects/<model("clinica_dental.clinica_dental"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinica_dental.object', {
#             'object': obj
#         })
