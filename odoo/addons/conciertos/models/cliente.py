# -*- coding: utf-8 -*-

from odoo import models, fields, api
   
class ConciertosCliente(models.Model):
    _name = 'sa.conciertos.cliente'
    _description = 'sa.conciertos.cliente'
    name = fields.Char('Nombre', required=True)
    email = fields.Char('Email')
    entradas_ids = fields.One2many('sa.conciertos.entrada', 'cliente_id', string='Entradas compradas')