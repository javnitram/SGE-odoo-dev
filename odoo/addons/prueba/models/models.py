# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PruebaCategoria(models.Model):
    _name = 'jf.prueba.categoria'
    _description = 'jf.prueba.categoria'
    name = fields.Char(string='Nombre',required=True,help='Introduce el nombre de la categoria')
    descripcion = fields.Text(string='Descripcion')


class PruebaLibro(models.Model):
    _name = 'jf.prueba.libro'
    name = fields.Char(string='Título',required=True,help='Introduce el nombre del libro')
    precio = fields.Float(string='Precio')
    ejemplares = fields.Integer(string='ejemplares')
    fecha = fields.Date(string='Fecha de compra')
    segmano = fields.Boolean(string='Segunda mano')
    estado = fields.Selection([
        ('0','Bueno'),('1','Regular'),('2','Malo')
    ], string='Estado',default="0")


    


# class prueba(models.Model):
#     _name = 'prueba.prueba'
#     _description = 'prueba.prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
