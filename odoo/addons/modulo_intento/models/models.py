# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Disco_Genero(models.Model):
    _name = 'yf.discos.genero'
    _description = 'discos.genero'
    nomcat = fields.Char('Nombre', required=True)

class Disco_Disco(models.Model):
    _name = 'yf.discos.disco'
    _description = 'discos.disco'
    titulo = fields.Char('titulo')
    precio = fields.Float('precio')

class Disco_Artista(models.Model):
    _name = 'yf.disco.artista'
    _description = 'disco.artista'
    nombre = fields.Char('nombre')

class Disco_Discografica(models.Model):
    _name = 'yf.disco.discografica'
    _description = 'disco.discografica'
    nombre = fields.Char('nombre')

class Disco_Cancion(models.Model):
    _name = 'yf.disco.cancion'
    _description = 'disco.cancion'
    nombre = fields.Char('nombre')
    duracion = fields.Float('duracion')
    album = fields.Char('album')
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
