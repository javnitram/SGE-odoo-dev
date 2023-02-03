# -*- coding: utf-8 -*-
# from odoo import http


# class ReBuy(http.Controller):
#     @http.route('/re_buy/re_buy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/re_buy/re_buy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('re_buy.listing', {
#             'root': '/re_buy/re_buy',
#             'objects': http.request.env['re_buy.re_buy'].search([]),
#         })

#     @http.route('/re_buy/re_buy/objects/<model("re_buy.re_buy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('re_buy.object', {
#             'object': obj
#         })
