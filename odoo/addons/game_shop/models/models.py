# -*- coding: utf-8 -*-

from odoo import models, fields, api


class game_shop_tienda(models.Model):
    _name = 'game_shop.tienda'
    _description = 'Tienda de videojuegos'
    name= fields.Char(string="Nombre",required=True,help="Introduce el nombre de la tienda")
    ubicacion = fields.Char(string="Ubicación",required=True,help="Introduce la ubicación de la tienda")
    horario = fields.Char(string ="Horario",help="Introduce el horario de la tienda",default="10:00")
    

class game_shop_videojuego(models.Model):
    _name = 'game_shop.videojuego'
    _description = 'Videojuego'
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de el videojuego")
    pegi= fields.Integer(string="Pegi",required=True,default=3,help="Introduce la edad minima para poder jugar al juego")
    precio = fields.Float(string="Precio",required=True,help="Introduce el precio del videojuego")    
    digital = fields.Boolean(string="Digital")
    estado = fields.Selection([
        ('0', 'Nuevo'),('1','Seminuevo'),('2','Usado')
    ], string='Estado', required=True,default="0")
    imagen = fields.Image(string="Imagen", max_width=640, max_height=480)

class game_shop_distribuidor(models.Model):
    _name = 'game_shop.distribuidor'
    _description = 'Distribuidor'
    name = fields.Char(string="Nombre", required=True,help="Introduce el nombre del distribuidor")
    sede = fields.Selection([
        ('0', 'Sevilla'),('1','Barcelona'),('2','Madrid'),
        ('3','Valencia'),('4','Santiago de Compostela'),('5','Valladolid'),
        ('6','Vitoria'),('7','Gran Canaria'),('8','Toledo'),
        ('9','Murcia'),('10','Zaragoza'),('11','Palma'),('12','Mérida'),
        ('13','Oviedo'),('14','Pamplona'),('15','Santander'),('16','Logroño'),
        ('17','Melilla'),('18','Ceuta')
    ], string='Sede',required=True,default="2")

class game_shop_almacen(models.Model):
    _name = 'game_shop.almacen'
    _description = 'Almacen juegos'
    name = fields.Char(string = "Almacen",required=True,help="Introduce el nombre del almacen",default="almacen")
    cantidad = fields.Integer(string = "Cantidad", help="Cantidad de juegos en el almacen",default=0)
    #fk juego

    


# class game_shop(models.Model):
#     _name = 'game_shop.game_shop'
#     _description = 'game_shop.game_shop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
