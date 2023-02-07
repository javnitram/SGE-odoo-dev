# -*- coding: utf-8 -*-
# from odoo import http


# class GameShop(http.Controller):
#     @http.route('/game_shop/game_shop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/game_shop/game_shop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('game_shop.listing', {
#             'root': '/game_shop/game_shop',
#             'objects': http.request.env['game_shop.game_shop'].search([]),
#         })

#     @http.route('/game_shop/game_shop/objects/<model("game_shop.game_shop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('game_shop.object', {
#             'object': obj
#         })
