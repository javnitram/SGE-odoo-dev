# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosConcierto(models.Model):
    _name = 'sa.conciertos.concierto'
    _description = 'sa.conciertos.concierto'
    name = fields.Char('Nombre')
    fecha = fields.Date('Fecha')
    artista_principal_id = fields.Many2one('sa.conciertos.artista', string='artista_principal')
    teloneros_ids = fields.Many2many('sa.conciertos.artista', string='Teloneros')
    recinto_id = fields.Many2one('sa.conciertos.recinto', string='Recinto', help='El recinto donde tendrá lugar')
    precio_base = fields.Float('Precio base por entrada')
    entradas_ids = fields.One2many('sa.conciertos.entrada', 'concierto_id', string='Entradas vendidas')
    dinero_recaudado = fields.Float(compute='_compute_dinero_recaudado', string='Dinero recaudado', store=True, default=0)
    
    @api.depends('entradas_ids', 'precio_base')
    def _compute_dinero_recaudado(self):
        for r in self:
            total = 0
            for entrada in r.entradas_ids:
                total += entrada.precio
            r.dinero_recaudado = total