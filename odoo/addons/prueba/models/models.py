# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pruebaCategoria(models.Model):
    _name = 'prueba.prueba_na'
    _description = 'prueba.prueba_des'


class pruebaPersona(models.Model):
    _name = 'prueba.persona.name'
    _description = 'prueba.persona.desc'
    name = fields.Char()
    age = fields.Integer()
    height = fields.Float()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
