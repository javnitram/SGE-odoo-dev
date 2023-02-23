# -*- coding: utf-8 -*-

# from odoo import models, fields, api
from odoo import models, fields, api

class TiendaMusicaCategoria(models.Model):
    _name = "irc.tienda_musica.categoria"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de la categoria")
    description = fields.Text(string="Descripción")
    cantants_ids = fields.Many2many("irc.tienda_musica.cantante", string="Cantantes")


class TiendaMusicaCD(models.Model):
    _name = "irc.tienda_musica.disco"
    name = fields.Char(string="Título",required=True,help="Introduce el título del album")
    precio = fields.Float(string="Precio")
    ejemplares = fields.Integer(string="ejemplares")
    fecha = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Bueno'),('1','Regular'),('2','Malo')],string="Estado",default="0")
    cantante_id = fields.Many2one("irc.tienda_musica.cantante",string="Cantante",required=True,ondelete="cascade")
    canciones_ids = fields.One2many("irc.tienda_musica.cancion", "disco_id", string="Canciones")


class TiendaMusicaCantante(models.Model):
    _name = "irc.tienda_musica.cantante"
    name = fields.Char(string="Nombre",required=True, help="Introduce el nombre del cantante")
    discos = fields.Char(string="Nombre del disco")
    nacionalidad = fields.Char(string="Nacionalidad del cantante")
    discos_ids = fields.One2many("irc.tienda_musica.disco", "cantante_id", string="Discos")
    generos_ids = fields.Many2many("irc.tienda_musica.categoria", string="Género")

class TiendaMusicaCancion(models.Model):
    _name = "irc.tienda_musica.cancion"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de la canción")
    artista = fields.Char(string="Cantante")
    album = fields.Char(string="Album")
    fecha = fields.Date(string="Fecha de salida")
    disco_id = fields.Many2one("irc.tienda_musica.disco", string="Album", required=True, ondelete="cascade")
    cancionimg = fields.Image(
        string="Imágen de la canción",
        store=True,
        relation="res.partner",
        help="Seleccionar imagen aquí"
    )
    
# class tienda_musica(models.Model):
#     _name = 'tienda_musica.tienda_musica'
#     _description = 'tienda_musica.tienda_musica'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
