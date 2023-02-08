# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ClubPadelClub(models.Model):
    _name = "clubpadel.club"
    _description = "Nombre del Club"
    name = fields.Char(string="Club",required=True,help="Introduce el nombre del club")

class ClubPadelMarca(models.Model):
    _name = "clubpadel.marca"
    _description = "Marca de la pala"
    name = fields.Char(string="Marca",required=True,help="Introduce el nombre de la marca")

class ClubPadelModelo(models.Model):
    _name = "clubpadel.modelo"
    _description = "Modelo de la pala"
    name = fields.Char(string="Modelo",required=True,help="Introduce el modelo de la pala")
    precio = fields.Float(string="Precio")
    versiones = fields.Selection([('0','Dura'),('1','Hibrida'),('2','Blanda')],string="Version",default="0")
    forma = fields.Selection([('0','Gota'),('1','Diamante'),('2','Redonda')],string="Forma",default="0")
    fecha = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Nuevo'),('1','Regular'),('2','Malo')],string="Estado",default="0")
class ClubPadelFabricante(models.Model):
    _name = "clubpadel.fabricante"
    _description = "Fabricante de la pala"
    name = fields.Char(string="Fabricante",required=True,help="Introduce el fabricante de la pala")
    fecha_salida = fields.Date(string="Fecha de salida")
    
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
