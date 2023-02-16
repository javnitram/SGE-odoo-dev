# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Disco_Genero(models.Model):
    _name = 'yf.discos.genero'
    _description = 'discos.genero'
    name = fields.Char('Nombre', required=True)
    canciones_ids = fields.One2many('yf.disco.cancion', 'genero_id', string='Canciones')

class Disco_Disco(models.Model):
    _name = 'yf.discos.disco'
    _description = 'discos.disco'
    name = fields.Char('titulo')
    precio = fields.Float('precio')
    artista_id = fields.Many2one("yf.disco.artista", string="artista", required=True)
    discografica_id = fields.Many2one("yf.disco.discografica", string='discografica')
    image = fields.Binary(string="portada")

class Disco_Artista(models.Model):
    _name = 'yf.disco.artista'
    _description = 'disco.artista'
    name = fields.Char('nombre')
    anhofundacion = fields.Char('año de fundacion')
    discografia_id = fields.One2many('yf.discos.disco', 'artista_id', string='Discografia')

class Disco_Discografica(models.Model):
    _name = 'yf.disco.discografica'
    _description = 'disco.discografica'
    name = fields.Char('nombre')
    anhofundacion = fields.Char('año de fundacion')

class Disco_Cancion(models.Model):
    _name = 'yf.disco.cancion'
    _description = 'disco.cancion'
    name = fields.Char('nombre')
    duracion = fields.Float('duracion')
    album_id = fields.Many2one("yf.discos.disco", string="album")
    artista_id = fields.Many2one("yf.disco.artista", string="artista")
    genero_id = fields.Many2one("yf.discos.genero", string="genero", required=True)

class DisqueraArtista(models.Model):
    _name = 'yf.disquera.artista'
    _description = 'Disqueras y sus esclavos'
    name = fields.Char('Pareja')
    anhocolaboracion = fields.Char('año de colaboracion')
    artistas_id = fields.Many2many("yf.disco.artista", string='Artistas')
    disqueras_id = fields.Many2many("yf.disco.discografica", string='Disqueras')



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
