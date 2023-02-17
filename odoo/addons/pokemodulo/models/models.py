# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemoduloEquipo1(models.Model):
     _name = 'ar.pokemodulo.equipo'
     _description = 'pokemodulo_equipo'
     Imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí")
     Nombre = fields.Char(string = 'Nombre de la Especie' ,required=True)
     Mote = fields.Char('Mote del Pokemon')
     Tipo1 = fields.Selection ([
         ('0','Agua'),
         ('1','Planta'),
         ('2', 'Fuego')
     ],string = 'Tipo1', required=True)
     Tipo2 = fields.Selection ([
         ('0','Null'),
         ('1','Electrico'),
         ('2','Fantasma'),
         ('3','Normal')
     ],string = 'Tipo2')




#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
