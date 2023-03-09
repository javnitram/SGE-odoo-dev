# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosArtista(models.Model):
    _name = 'sa.conciertos.artista'
    _description = 'sa.conciertos.artista'
    name = fields.Char('Nombre', required=True)
    foto = fields.Image('Foto', max_width=200, max_height=200)
    conciertos_propios_ids = fields.One2many('sa.conciertos.concierto', 'artista_principal_id', string='Conciertos propios')
    otros_conciertos_ids = fields.Many2many('sa.conciertos.concierto', string='Conciertos (como telonero)')
 