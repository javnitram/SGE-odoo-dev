# -*- coding: utf-8 -*-

from odoo import models, fields, api


class game_shop_tienda(models.Model):
    _name = 'sb_game_shop.tienda'
    _description = 'Tienda de videojuegos'
    name= fields.Char(string="Nombre",required=True,help="Introduce el nombre de la tienda")
    calle = fields.Char(string="Calle",required=True,help="Introduce la calle de la tienda")
    horario = fields.Char(string ="Horario",help="Introduce el horario de la tienda",default="10:00")
    almacen_id = fields.Many2one('sb_game_shop.almacen', string="Almacen de la tienda")
    videojuegos_ids = fields.Many2many('sb_game_shop.videojuego', string="Videojuegos disponibles")

class game_shop_videojuego(models.Model):
    _name = 'sb_game_shop.videojuego'
    _description = 'Videojuego'
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de el videojuego")
    pegi= fields.Integer(string="Pegi",required=True,default=3,help="Introduce la edad minima para poder jugar al juego")
    precio = fields.Float(string="Precio Unitario",required=True,help="Introduce el precio del videojuego")    
    digital = fields.Boolean(string="Digital")
    estado = fields.Selection([
        ('0', 'Nuevo'),('1','Seminuevo'),('2','Usado')
    ], string='Estado', required=True,default="0")
    imagen = fields.Image(string="Imagen", max_width=640, max_height=480)
    distribuidor_id = fields.Many2one('sb_game_shop.distribuidor', string="Distribuidor del juego")
    tiendas_ids = fields.Many2many('sb_game_shop.tienda', string='Tiendas disponibles')
    precio_iva = fields.Float(string="Precio con IVA",help="Precio calculado con el IVA", compute="_precioIVA",store=True)
    @api.depends('precio','digital')
    def _precioIVA(self):
        for i in self:
            if i.digital:
                i.precio_iva = (i.precio-5)*1.21
            else:
                i.precio_iva = i.precio*1.21

class game_shop_distribuidor(models.Model):
    _name = 'sb_game_shop.distribuidor'
    _description = 'Distribuidor'
    name = fields.Char(string="Nombre", required=True,help="Introduce el nombre del distribuidor")
    pais_id = fields.Many2one('res.country', string='Pais')
    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    videojuegos_ids = fields.One2many('sb_game_shop.videojuego', 'distribuidor_id', string="Juegos que son distribuidos")

class game_shop_almacen(models.Model):
    _name = 'sb_game_shop.almacen'
    _description = 'Almacen juegos'
    name = fields.Char(string = "Almacen",required=True,help="Introduce el nombre del almacen",default="almacen")
    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    calle = fields.Char(string="Calle", help="Introduce el nombre de la calle")
    tiendas_ids = fields.One2many('sb_game_shop.tienda', 'almacen_id', string="Tiendas a la que suminsitra")
