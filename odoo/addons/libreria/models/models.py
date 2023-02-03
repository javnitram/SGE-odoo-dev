# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibreriaCategoria(models.Model):
    _name = 'jm.libreria.categoria'
    _description = 'Modelo categoría'
    name = fields.Char('Nombre',required=True, help='Introduce nombre de la categoría')
    description = fields.Char('Descripción')

class LibreriaLibro(models.Model):
    _name = 'jm.libreria.libro'
    _description = 'Modelo libro'
    name = fields.Char('Título')
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha = fields.Date('Fecha')
    segunda_mano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado')

class LibreriaAutor(models.Model):
    _name = 'jm.libreria.autor'
    _description = 'Modelo autor'
    name = fields.Char('Nombre', required=True, help="Introduce el nombre del autor")
    
     

# class libreria(models.Model):
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
