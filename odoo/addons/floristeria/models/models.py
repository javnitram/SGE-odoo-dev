# -*- coding: utf-8 -*-

from odoo import models, fields, api

class floristeria(models.Model):
    _name = 'floristeria.floristeria'
    _description = 'Floristeria'

class flower(models.Model):
    _name = 'hf_floristeria_flower'
    _description = 'Flor'
    name = fields.Char(string='Nombre común',required=True, help='')
    scientific_name = fields.Char(string='Nombre científico', help='')
    specie = fields.Char(string='Especie', help='')
    main_color = fields.Char(string='Color predominante', help='')
    """ group = fields.Selection([
        ('A', 'Angiospermas'),
        ('G', 'Gimnospermas')
    ], string='Grupo',required=True)
    subgroup = fields.Selection([
        ('0', 'Cícadas'),
        ('1', 'Ginko'),
        ('2', 'Coníferas'),
        ('3', 'Gnetales')
    ], string='Subgrupo',required=True) """

class bouquet(models.Model):
    _name = 'hf_floristeria_bouquet'
    _description = 'Ramo de flores'
    size = fields.Char('Tamaño', required=True)
    price = fields.Float('Precio', required=True)
    delivery_date = fields.Date('Fecha de entrega')
