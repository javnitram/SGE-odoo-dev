# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibreriaCategoria(models.Model):
    _name = "libreria.categoria"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de la categoria")
    description = fields.Text(string="Descripción")
    libros_ids = fields.One2many('libreria.libro', 'categoria_id', string='Libros de la categoría')

class LibreriaLibro(models.Model):
    _name = "libreria.libro"
    name = fields.Char(string="Título",required=True,help="Introduce el título del libro")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="ejemplares")
    fecha = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default="0")
    categoria_id = fields.Many2one('libreria.categoria', string='Categoría')
    autores_ids = fields.Many2many('libreria.autor', string='Autores')

class LibreriaAutor(models.Model):
    _name="libreria.autor"
    _description= "Modelo Autor"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre del autor")
    libros_ids = fields.Many2many('libreria.libro', string='Libros de autores')
