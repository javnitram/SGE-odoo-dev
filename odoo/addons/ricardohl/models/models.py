# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuloProducto(models.Model):
    _name = 'rh.producto.name'
    _description = 'rh.producto.name'
    nombre_producto = fields.Char('NombreProdcuto',required=True,help='Introduce el nombre del producto')
    precio = fields.Integer('Precio')

class ModuloCliente(models.Model):
    _name = 'rh.cliente.name'
    _description = 'rh.cliente.name'
    nombre_cliente = fields.Char('NombreCliente',required=True,help='Introduce el nombre del cliente')
    
class ModuloEspecieAnimal(models.Model):
    _name = 'rh.animal.name'
    _description = 'rh.animal.name'
    nombre_animal = fields.Char('NombreAnimal',required=True,help='Introduce el nombre común de la especie del animal')
    nombre_cien = fields.Char('NombreCien',required=True,help='Introduce el nombre científico de la especie del animal')
    
class ModuloEspecieVegetal(models.Model):
    _name = 'rh.vegetal.name'
    _description = 'rh.vegetal.name'
    nombre_vegetal = fields.Char('NombreVegetal',required=True,help='Introduce el nombre común de la especie del vegetal')
    nombre_cien = fields.Char('NombreCien',required=True,help='Introduce el nombre científico de la especie del vegetal')



# class ricardohl(models.Model):
#     _name = 'ricardohl.ricardohl'
#     _description = 'ricardohl.ricardohl'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
