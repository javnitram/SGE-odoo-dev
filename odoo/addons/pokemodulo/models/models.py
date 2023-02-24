# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemoduloEquipoIndi(models.Model):
     _name = 'ar.pokemodulo.equipoi'
     _description = 'pokemodulo_equipoi'
     NombreEquipo = fields.Char(string = 'Nombre de Equipo' ,required=True)
     NombreEntrenador = fields.Many2one('ar.pokemodulo.entrenadores', string='Nombre del entrenador')
#     Poke1 =
#     Poke2 = 
#     Poke3 =
#     Poke4 =
#     Poke5 =
#     Poke6 =
    



class pokemoduloEquipoDobles(models.Model):
     _name = 'ar.pokemodulo.equipod'
     _description = 'pokemodulo_equipod'
     NombreEquipo = fields.Char(string = 'Nombre de Equipo' ,required=True)
     NombreEntrenador = fields.Many2one('ar.pokemodulo.entrenadores', string='Nombre del entrenador')
#     Poke1 =
#     Poke2 = 
#     Poke3 =
#     Poke4 =
#     Poke5 =
#     Poke6 =
 



class pokemoduloPokemon(models.Model):
     _name = 'ar.pokemodulo.pokemon'
     _description = 'pokemodulo_pokemon'
     Imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí", required=True)
     Nombre = fields.Char(string = 'Nombre de la Especie' ,required=True)
     Generacion = fields.Integer('Generacion', required=True)
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
     name = fields.Char(string = 'Nombre del entrenador', required=True)



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
