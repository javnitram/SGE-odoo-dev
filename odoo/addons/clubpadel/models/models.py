# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError


class ClubPadelClub(models.Model):
    _name = "ab_clubpadel.club"
    _description = "Nombre del Club"
    _translate = "True"
    nombre = fields.Char(string="Club",required=True,help="Introduce el nombre del club.")
    pais_id = fields.Many2one('res.country', string='Pais')
    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    marcas_ids = fields.Many2many('ab_clubpadel.marca', string='Marcas del club')

class ClubPadelFabricante(models.Model):
    _name = "ab_clubpadel.fabricante"
    _description = "Fabricante de la pala"
    name = fields.Char(string="Fabricante",required=True,help="Introduce el fabricante de la pala")
    fecha_salida = fields.Date(string="Fecha de salida")
    pais_id = fields.Many2one('res.country', string='Pais')
    provincia_id = fields.Many2one('res.country.state', string='Provincia')
    marcas_ids = fields.One2many('ab_clubpadel.marca', 'fabricante_id', string='Marcas del fabricante')

class ClubPadelMarca(models.Model):
    _name = "ab_clubpadel.marca"
    _description = "Marca de la pala"
    name = fields.Char(string="Marca",help="Introduce el nombre de la marca")
    imagen = fields.Image('Imagen', max_width=400, max_height=300)
    fecha = fields.Date(string="Fecha de creación")
    gama = fields.Char(string="Gama",required=True,help="Gama de la marca.")
    models_ids = fields.One2many('ab_clubpadel.modelo', 'marca_id', string='Modelos de la marca')
    fabricante_id = fields.Many2one("ab_clubpadel.fabricante", string="Fabricante de la marca", required=True)
    clubes_ids = fields.Many2many('ab_clubpadel.club', string='Clubes de la marca')
    @api.constrains('name')
    def _checkNombre(self):
        if not self.name:
            raise ValidationError("Debes escribir un nombre para la Marca.")

class ClubPadelModelo(models.Model):
    _name = "ab_clubpadel.modelo"
    _description = "Modelo de la pala"
    name = fields.Char(string="Modelo",required=True,help="Introduce el modelo de la pala")
    precio = fields.Float(string="Precio")
    versiones = fields.Selection([('0','Dura'),('1','Hibrida'),('2','Blanda')],string="Version",default="0")
    forma = fields.Selection([('0','Gota'),('1','Diamante'),('2','Redonda')],string="Forma",default="0")
    fecha = fields.Date(string="Fecha de salida")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Nuevo'),('1','Regular'),('2','Malo')],string="Estado",default="0")
    marca_id = fields.Many2one("ab_clubpadel.marca", string="Marca del modelo", required=True)
    precio_final = fields.Float(string="Precio final", compute="_preciofinal", store=True)
    @api.depends('precio','segmano')
    def _preciofinal(self):
        for i in self:
            if i.segmano:
                i.precio_final = i.precio/2
            else:
                i.precio_final = i.precio

    
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
