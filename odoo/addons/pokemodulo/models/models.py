# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemoduloEquipo1(models.Model):
     _name = 'ar.pokemodulo.equipo1'
     _description = 'pokemodulo_equipo'
     Imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí", required=True)
     Nombre = fields.Char(string = 'Nombre de la Especie' ,required=True)
     Mote = fields.Char('Mote del Pokemon')
     Tipo1 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo1', required=True)
     Tipo2 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo2')
     

class pokemoduloEquipo2(models.Model):
     _name = 'ar.pokemodulo.equipo2'
     _description = 'pokemodulo_equipo2'
     Imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí", required=True)
     Nombre = fields.Char(string = 'Nombre de la Especie' ,required=True)
     Mote = fields.Char('Mote del Pokemon')
     Tipo1 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo1', required=True)
     Tipo2 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo2')




class pokemoduloEquipo3(models.Model):
     _name = 'ar.pokemodulo.equipo3'
     _description = 'pokemodulo_equipo3'
     Imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí", required=True)
     Nombre = fields.Char(string = 'Nombre de la Especie' ,required=True)
     Mote = fields.Char('Mote del Pokemon')
     Tipo1 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo1', required=True)
     Tipo2 = fields.Selection ([
         ('0','Acero'),
         ('1','Agua'),
         ('2', 'Bicho'),
         ('3', 'Dragon'),
         ('4', 'Electrico'),
         ('5', 'Fantasma'),
         ('6', 'Fuego'),
         ('7', 'Hada'),
         ('8', 'Hielo'),
         ('9', 'Lucha'),
         ('10', 'Normal'),
         ('11', 'Planta'),
         ('12', 'Psiquico'),
         ('13', 'Roca'),
         ('14', 'Siniestro'),
         ('15', 'Tierra'),
         ('16', 'Veneno'),
         ('17', 'Volador')
     ],string = 'Tipo2')







class pokemoduloEntrenadores(models.Model):
     _name = 'ar.pokemodulo.entrenadores'
     _description = 'pokemodulo_entrenadores'
     ImagenE = fields.Image(string="Imagen Entrenador",store=True,relation="res.partner",help="Seleccionar imagen aquí", required=True)
     Nombre = fields.Char(string = 'Nombre del entrenador', required=True)
     campo = fields.Char('campo')



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
