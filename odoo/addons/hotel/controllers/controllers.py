# -*- coding: utf-8 -*-
# from odoo import http


# class Hotel(http.Controller):
#     @http.route('/hotel/hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel/hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel.listing', {
#             'root': '/hotel/hotel',
#             'objects': http.request.env['hotel.hotel'].search([]),
#         })

#     @http.route('/hotel/hotel/objects/<model("hotel.hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel.object', {
#             'object': obj
#         })
