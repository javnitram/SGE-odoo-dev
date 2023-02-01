# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibreriaCategoria(models.Model):
    _name = 'sa.libreria.categoria'
    _description = 'sa.libreria.categoria'
    nombre = fields.Char('nombre', required=True)
    name = fields.Char(string="Nombre", required=True, help="Introduce el nombre de la categoria")
    descripcion = fields.Text(string="Descripción")
    

class LibreriaLibro(models.Model):
    _name = 'sa.libreria.libro'
    _description = 'sa.libreria.libro'
    name = fields.Char(string="Título",required=True,help="Introduce el título del libro")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="Ejemplares")
    fecha = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([
        ('0', 'Bueno'), ('1', 'Regular'), ('2', 'Malo')
    ], string='estado')

# class librer, required=Trueia(models.Model):
#     _name = 'libreria.libreria'
#     _description = 'libreria.libreria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
