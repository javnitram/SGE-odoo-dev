# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosArtista(models.Model):
    _name = 'sa.conciertos.artista'
    _description = 'sa.conciertos.artista'
    name = fields.Char('Nombre', required=True)
    conciertos_propios_ids = fields.One2many('sa.conciertos.concierto', 'artista_principal_id', string='Conciertos propios')
    otros_conciertos_ids = fields.Many2many('sa.conciertos.concierto', string='Conciertos (como telonero)')
    foto = fields.Image('Foto', max_width=200, max_height=200)

class ConciertoRecinto(models.Model):
    _name = 'sa.conciertos.recinto'
    _description = 'sa.conciertos.recinto'
    name = fields.Char('Nombre')
    ciudad = fields.Char('Ciudad')
    pais_id = fields.Many2one('res.country', string='País')
    capacidad = fields.Integer('Capacidad')
    conciertos_ids = fields.One2many('sa.conciertos.concierto', 'recinto_id', string='Conciertos')
    
class ConciertosCliente(models.Model):
    _name = 'sa.conciertos.cliente'
    _description = 'sa.conciertos.cliente'
    name = fields.Char('Nombre')
    email = fields.Char('Email')
