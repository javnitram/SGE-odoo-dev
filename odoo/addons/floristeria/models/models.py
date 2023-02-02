# -*- coding: utf-8 -*-

from odoo import models, fields, api

class floristeria(models.Model):
    _name = 'floristeria.floristeria'
    _description = 'Floristeria'

class flower(models.Model):
    _name = 'hf_floristeria_flower'
    _description = 'Flor'
    name = fields.Char('Flor')

class bouquet(models.Model):
    _name = 'hf_floristeria_bouquet'
    _description = 'Ramo de flores'
    
