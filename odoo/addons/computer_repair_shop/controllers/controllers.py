# -*- coding: utf-8 -*-
# from odoo import http


# class ComputerRepairShop(http.Controller):
#     @http.route('/computer_repair_shop/computer_repair_shop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/computer_repair_shop/computer_repair_shop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('computer_repair_shop.listing', {
#             'root': '/computer_repair_shop/computer_repair_shop',
#             'objects': http.request.env['computer_repair_shop.computer_repair_shop'].search([]),
#         })

#     @http.route('/computer_repair_shop/computer_repair_shop/objects/<model("computer_repair_shop.computer_repair_shop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('computer_repair_shop.object', {
#             'object': obj
#         })
