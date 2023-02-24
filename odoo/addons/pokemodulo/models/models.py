# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pokemoduloEquipoIndi(models.Model):
     _name = 'ar.pokemodulo.equipoi'
     _description = 'pokemodulo_equipoi'
     name = fields.Char(string = 'Nombre de Equipo' ,required=True, help='Inserte el nombre del equipo')
     NombreEntrenador = fields.Many2one('ar.pokemodulo.entrenadores', string='Nombre del entrenador', required=True, help='Inserte el popietario del equipo')
     Pokemones =fields.Many2many('ar.pokemodulo.pokemon', string='Nombre de los pokemons', required=True, help='Inserte a los pokemons, si no hay, crealos')

    



class pokemoduloEquipoDobles(models.Model):
     _name = 'ar.pokemodulo.equipod'
     _description = 'pokemodulo_equipod'
     name = fields.Char(string = 'Nombre de Equipo' ,required=True, help='Inserte el nombre del equipo')
     NombreEntrenador = fields.Many2one('ar.pokemodulo.entrenadores', string='Nombre del entrenador' ,required=True, help='Inserte el popietario del equipo')
     Pokemones =fields.Many2many('ar.pokemodulo.pokemon', string='Nombre de los pokemons',required=True, help='Inserte a los pokemons, si no hay, crealos')

 



class pokemoduloPokemon(models.Model):
     _name = 'ar.pokemodulo.pokemon'
     _description = 'pokemodulo_pokemon'
     Imagen = fields.Image(string="Imagen Pokémon",store=True,relation="res.partner",help="Insertar Imagen", required=True, help='Pon aqui la imagen de la especie del pokémon')
     name = fields.Char(string = 'Nombre de la Especie' ,required=True, help='Inserte el nombre de la especie')
     Generacion = fields.Integer('Generacion', required=True, help='Inserte su generacion, ejemplo: 1 , 2 , 3 , 4 , etc...')
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
     ImagenE = fields.Image(string="Imagen Entrenador",store=True,relation="res.partner",help="Seleccionar imagen del entrenador aquí", required=True)
     name = fields.Char(string = 'Nombre del entrenador', required=True, help='Insertar nombre del entrenador')
     EquiposI = fields.One2many('ar.pokemodulo.equipoi', 'NombreEntrenador' , string='Equipo Individuales' )
     EquiposD = fields.One2many('ar.pokemodulo.equipod', 'NombreEntrenador' , string='Equipo Dobles' )


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
