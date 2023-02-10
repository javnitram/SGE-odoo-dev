# -*- coding: utf-8 -*-

from odoo import models, fields, api


class libreriaCategoria(models.Model):
    _name = 'ar.libreria.categoria'
    _description = 'libreria Categoria'
    name = fields.Char(string='Nombre',required=True,help='Introduce el título de la categoria')
    description = fields.Char('Descripcion')
    precio = fields.Float('Precio')

class libreriaLibro(models.Model):
    _name = 'ar.libreria.libro'
    _description = 'Libreria Libro'
    name = fields.Char(string='Título')
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha = fields.Date('Fecha')
    

class libreriaAutor(models.Model):
    _name = 'ar.libreria.autor'
    _description='Modelo autor'
    name = fields.Char(string='Nombre Autor')
    

class editorialLibro(models.Model):
    _name = 'ar.libreria.editorial'
    _description = 'Modelo Editorial'
    name = fields.Char('Nombre')
    fundacion = fields.Date('fecha de nacimiento')



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
