# -*- coding: utf-8 -*-

from odoo import models, fields, api

<<<<<<< HEAD

class LibreriaCategoria(models.Model):
    _name = 'jm.libreria.categoria'
    _description = 'Modelo categoría'
    name = fields.Char('Nombre',required=True, help='Introduce nombre de la categoría')
    description = fields.Char('Descripción')
    libros_ids = fields.One2many('jm.libreria.libro', 'categoria_id', string='Libros de la categoría')


class LibreriaLibro(models.Model):
    _name = 'jm.libreria.libro'
    _description = 'Modelo libro'
    name = fields.Char('Título')
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha = fields.Date('Fecha')
=======
  
class LibreriaCategoria(models.Model):
    _name = 'jm.libreria.categoria'
    _description = 'Categoría de libros'
    name = fields.Char('Nombre')
    libros_ids = fields.One2many('jm.libreria.libro', 'categoria_id', string='Libros de la categoría')
    field_name_ids = fields.One2many('comodel_name', 'inverse_field_name', string='field_name')
    total_libros_categoria = fields.Char(compute='_calculo_total_libros_categoria', string='Total libros')
    
    @api.depends('')
    def _calculo_total_libros_categoria(self):
        pass

class LibreriaLibro(models.Model):
    _name = 'jm.libreria.libro'
    _description = 'Libro'
    name = fields.Char('Título', required=True, help='Introduce título del libro')
    precio = fields.Float('Precio')
>>>>>>> ff821938758c0a4298fbccc1c7352ee046627224
    segunda_mano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regular'),
        ('2', 'Malo')
    ], string='Estado')
    categoria_id = fields.Many2one('jm.libreria.categoria', string='Categoría')
<<<<<<< HEAD
    autores_ids = fields.Many2many('jm.libreria.autor', string='Autores')

class LibreriaAutor(models.Model):
    _name = 'jm.libreria.autor'
    _description = 'Modelo autor'
    name = fields.Char('Nombre', required=True, help="Introduce el nombre del autor")
    fecha = fields.Date('Fecha de nacimiento', help="Introduce fecha de nacimiento del autor")
    libros_ids = fields.Many2many('jm.libreria.libro', string='Libros del autor')
    pais_id = fields.Many2one('res.country', string='País')
    
=======
    pais_publicacion_id = fields.Many2one('res.country', string='País de publicación')
    autores_ids = fields.Many2many('jm.libreria.autor', string='Autores')
    
class LibreriaAutor(models.Model):
    _name = 'jm.libreria.autor'
    _description = 'Autor'
    name = fields.Char('Autor', required=True, help='Introduce el nombre del autor')
    fec_nacimiento = fields.Date('Fecha de nacimiento')
    pais_id = fields.Many2one('res.country', string='País')
    libros_ids = fields.Many2many('jm.libreria.libro', string='Libros')
    

>>>>>>> ff821938758c0a4298fbccc1c7352ee046627224
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
