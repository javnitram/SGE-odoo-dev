# -*- coding: utf-8 -*-

from odoo import models, fields, api

class floristeria(models.Model):
    _name = 'hf_floristeria_floristeria'
    _description = 'Floristeria'
    name = fields.Char('Nombre')

class flower(models.Model):
    _name = 'hf_floristeria_flower'
    _description = 'Flor'
    name = fields.Char(string='Nombre común',required=True, help='')
    scientific_name = fields.Char(string='Nombre científico', required=True, help='')
    specie = fields.Char(string='Especie', required=True, help='')
    main_color = fields.Char(string='Color predominante', help='')
    group = fields.Selection([
        ('0', ''),
        ('A', 'Angiospermas'),
        ('G', 'Gimnospermas')
    ], string='Grupo',required=True)
    """ subgroup = fields.Selection([
        ('0', 'Cícadas'),
        ('1', 'Ginko'),
        ('2', 'Coníferas'),
        ('3', 'Gnetales')
    ], string='Subgrupo',required=True) """
    image = fields.Image('Imagen')

class bouquet(models.Model):
    _name = 'hf_floristeria_bouquet'
    _description = 'Ramo de flores'
    name = fields.Char('Nombre', required=True)
    size = fields.Selection([
        ('0', ''),
        ('1', 'Pequeño'),
        ('2', 'Normal'),
        ('3', 'Grande'),
        ('4', 'Enorme')
    ], string='Tamaño',required=True)
    price = fields.Float('Precio', required=True)
    delivery_date = fields.Date('Fecha de entrega')
    image = fields.Image('Imagen')
