# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClubPadelClub(models.Model):
    _name = "clubpadel.club"
    _description = "Nombre del Club"
    nombre = fields.Char(string="Club",required=True,help="Introduce el nombre del club.")
    ubicacion = fields.Char(string="Ubicacion",required=True,help="Introduce la ubicacion del club.")
    marcas_ids = fields.Many2many('clubpadel.marca', string='Marcas del club')

class ClubPadelFabricante(models.Model):
    _name = "clubpadel.fabricante"
    _description = "Fabricante de la pala"
    name = fields.Char(string="Fabricante",required=True,help="Introduce el fabricante de la pala")
    fecha_salida = fields.Date(string="Fecha de salida")
    ubicacion = fields.Char(string="Ubicacion",required=True,help="Introduce la ubicacion del fabricante.")
    marcas_ids = fields.One2many('clubpadel.marca', 'fabricante_id', string='Marcas del fabricante')

class ClubPadelMarca(models.Model):
    _name = "clubpadel.marca"
    _description = "Marca de la pala"
    name = fields.Char(string="Marca",required=True,help="Introduce el nombre de la marca")
    imagen = fields.Image('Imagen', max_width=400, max_height=300)
    fecha = fields.Date(string="Fecha de creación")
    gama = fields.Char(string="Gama",required=True,help="Gama de la marca.")
    models_ids = fields.One2many('clubpadel.modelo', 'marca_id', string='Modelos de la marca')
    fabricante_id = fields.Many2one("clubpadel.fabricante", string="Fabricante de la marca", required=True)
    clubes_ids = fields.Many2many('clubpadel.club', string='Clubes de la marca')

class ClubPadelModelo(models.Model):
    _name = "clubpadel.modelo"
    _description = "Modelo de la pala"
    name = fields.Char(string="Modelo",required=True,help="Introduce el modelo de la pala")
    precio = fields.Float(string="Precio")
    versiones = fields.Selection([('0','Dura'),('1','Hibrida'),('2','Blanda')],string="Version",default="0")
    forma = fields.Selection([('0','Gota'),('1','Diamante'),('2','Redonda')],string="Forma",default="0")
    fecha = fields.Date(string="Fecha de salida")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Nuevo'),('1','Regular'),('2','Malo')],string="Estado",default="0")
    marca_id = fields.Many2one("clubpadel.marca", string="Marca del modelo", required=True)
    
# class clubpadel(models.Model):
#     _name = 'clubpadel.clubpadel'
#     _description = 'clubpadel.clubpadel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
