# -*- coding: utf-8 -*-

from odoo import models, fields, api

  
class LibreriaCategoria(models.Model):
    _name = 'jm.libreria.categoria'
    _description = 'Categoría de libros'
    name = fields.Char('Nombre')

class LibreriaLibro(models.Model):
    _name = 'jm.libreria.libro'
    _description = 'Libro'
    name = fields.Char('Título', required=True, help='Introduce título del libro')
    precio = fields.Float('Precio')
    segunda_mano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado')
    categoria_id = fields.Many2one('jm.libreria.categoria', string='Categoría')
    autores_ids = fields.Many2many('jm.libreria.autor', string='Autores')
    
class LibreriaAutor(models.Model):
    _name = 'jm.libreria.autor'
    _description = 'Autor'
    name = fields.Char('Autor', required=True, help='Introduce el nombre del autor')
    fec_nacimiento = fields.Date('Fecha de nacimiento')
    pais_id = fields.Many2one('res.country', string='País')
    

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
