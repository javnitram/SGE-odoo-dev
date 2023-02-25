# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertoRecinto(models.Model):
    _name = 'sa.conciertos.recinto'
    _description = 'sa.conciertos.recinto'
    name = fields.Char('Nombre', required=True)
    ciudad = fields.Char('Ciudad')
    pais_id = fields.Many2one('res.country', string='País')
    capacidad = fields.Integer('Capacidad', required=True)
    conciertos_ids = fields.One2many('sa.conciertos.concierto', 'recinto_id', string='Conciertos')

    # Campos calculados
    currency_id = fields.Many2one('res.currency', compute='_compute_currency_id', string='Divisa')
    
    @api.depends('pais_id')
    def _compute_currency_id(self):
        for r in self:
            r.currency_id = r.pais_id.currency_id