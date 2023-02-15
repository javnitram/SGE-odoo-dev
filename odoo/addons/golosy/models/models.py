# -*- coding: utf-8 -*-

from odoo import models, fields, api


class golosinas(models.Model):
     _name = 'wb.golosy.golosinas'
     _description = 'Nombre y lista de golosinas'

     id_asig = fields.Integer('id_golosina', required=True, help="Identificador de la golosina")
     name = fields.Char('Nombre', required=True, help='Nombre de la golosina')
     precio = fields.Float('Precio', required=True, help='precio de la golosina')
     description = fields.Text()

class cantidades(models.Model):
     _name = 'wb.golosy.cantidades'
     _description = 'Cantidad de cada golosina'

     id_asig = fields.Integer('id_golosina', required=True, help="Identificador de la golosina")
     cantidad = fields.Integer('Cantidad', required=True, help='Cantidad stock de la golosina')
     camion = fields.Selection([
        ('0', 'Solicitar al camión'),
        ('1', 'Dar de baja al producto')
     ], string='¿Solicitar al camion nuevo envio?')
     
class stock(models.Model):
     _name = 'wb.golosy.stock'
     _description = 'Stock de las golosinas'

     stock_total = fields.Integer('Stock', required=True, help='Stock total de las golosinas')
     stock_tipo = fields.Selection([
        ('0', 'Azucaradas'),
        ('1', 'Sin azucar')
        ('2', 'Otros')
     ], string='Cantidades divido en los tipos de golosinas')
