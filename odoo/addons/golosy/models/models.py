# -*- coding: utf-8 -*-

from odoo import models, fields, api


class golosinas(models.Model):
     _name = 'wb.golosy.golosinas'
     _description = 'Nombre y lista de golosinas'

     name = fields.Char('Nombre', required=True, help='Nombre de la golosina')
     precio = fields.Float('Precio', required=True, help='precio de la golosina')
     cantidad = fields.Integer('Cantidad', required=True, help='Cantidad stock de la golosina')
     description = fields.Text()
     camion = fields.Selection([
        ('0', 'Solicitar al camión'),
        ('1', 'Dar de baja al producto')
     ], string='¿Solicitar al camion nuevo envio?')

#No valido
class cantidades(models.Model):
     _name = 'wb.golosy.cantidades'
     _description = 'Cantidad de cada golosina'

     name = fields.Char('Nombre', required=True, help='Nombre de la golosina')
     id_asig = fields.Integer('id_golosina', required=True, help="Identificador de la golosina")
     cantidad = fields.Integer('Cantidad', required=True, help='Cantidad stock de la golosina')
     camion = fields.Selection([
        ('0', 'Solicitar al camión'),
        ('1', 'Dar de baja al producto')
     ], string='¿Solicitar al camion nuevo envio?')
     
#No valido
class stock(models.Model):
     _name = 'wb.golosy.stock'
     _description = 'Stock de las golosinas'

     stock_total = fields.Integer('Stock', required=True, help='Stock total de las golosinas')
     stock_tipo = fields.Selection([
        ('0', 'Azucaradas'),
        ('1', 'Sin azucar'),
        ('2', 'Otros')
     ], string='Cantidades divido en los tipos de golosinas')

class categorias(models.Model):
     _name = 'wb.golosy.categoria'
     _description = 'Categorias de las golosinas'

     name = fields.Char('Categoria', required=True, help='Nombre de la categoria')
     tipo = fields.Selection([
        ('0', 'Dulce'),
        ('1', 'Salado')
     ], string='Tipo de la categoria')
     
class Camion(models.Model):
     _name = 'wb.golosy.camion'
     _description = 'Solicitudes al camion'

     name = fields.Char('Pedido', required=True, help='Nombre de la pedido')
     productos = fields.Integer('Productos', required=True, help='Productos a pedir')
