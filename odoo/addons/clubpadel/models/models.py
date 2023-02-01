# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClubPadelMarca(models.Model):
    _name = "clubpadel.marca"
    _description = "Marca de la pala"
    name = fields.Char(string="Nombre",required=True,help="Introduce el nombre de la marca")
class ClubPadelModelo(models.Model):
    _name = "clubpadel.modelo"
    _description = "Modelo de la pala"
    name = fields.Char(string="Título",required=True,help="Introduce el modelo de la pala")
    precio = fields.Float(string="Precio")
    versiones = fields.Selection([('0','Dura'),('1','Hibrida'),('2','Blanda')],string="Version",default="0")
    forma = fields.Selection([('0','Gota'),('0','Diamante'),('0','Redonda')],string="Forma",default="0")
    fecha = fields.Date(string="Fecha de compra")
    segmano = fields.Boolean(string="Segunda mano")
    estado = fields.Selection([('0','Nuevo'),('1','Regular'),('2','Malo')],string="Estado",default="0")
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
