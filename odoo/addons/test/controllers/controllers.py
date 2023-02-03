# -*- coding: utf-8 -*-
# from odoo import http


# class Test(http.Controller):
#     @http.route('/test/test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test/test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test.listing', {
#             'root': '/test/test',
#             'objects': http.request.env['test.test'].search([]),
#         })

#     @http.route('/test/test/objects/<model("test.test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test.object', {
#             'object': obj
#         })
