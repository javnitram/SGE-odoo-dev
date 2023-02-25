# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosConcierto(models.Model):
    _name = 'sa.conciertos.concierto'
    _description = 'sa.conciertos.concierto'

    # Datos y artistas
    name = fields.Char('Nombre')
    fecha = fields.Date('Fecha', required=True)
    artista_principal_id = fields.Many2one('sa.conciertos.artista', string='Artista principal', 
                                           required=True)
    teloneros_ids = fields.Many2many('sa.conciertos.artista', string='Teloneros')
    recinto_id = fields.Many2one('sa.conciertos.recinto', string='Recinto', 
                                 help='El recinto donde tendrá lugar el concierto', required=True)
    
    # Venta
    precio_base = fields.Monetary('Precio base por entrada', required=True)
    entradas_ids = fields.One2many('sa.conciertos.entrada', 'concierto_id')

    # Campos calculados
    currency_id = fields.Many2one('res.currency', compute='_compute_currency_id', string='Divisa')
    entradas_vendidas = fields.Integer(compute='_compute_entradas_vendidas', string='Entradas vendidas')
    entradas_disponibles = fields.Integer(compute='_compute_entradas_disponibles', 
                                          string='Entradas disponibles')
    dinero_recaudado = fields.Monetary(compute='_compute_dinero_recaudado', string='Dinero recaudado', 
                                       store=True, default=0)
    
    @api.depends('recinto_id.currency_id')
    def _compute_currency_id(self):
        for r in self:
            r.currency_id = r.recinto_id.currency_id

    @api.depends('entradas_ids', 'precio_base')
    def _compute_dinero_recaudado(self):
        for r in self:
            total = 0
            for entrada in r.entradas_ids:
                total += entrada.precio
            r.dinero_recaudado = total
    
    @api.depends('entradas_ids')
    def _compute_entradas_vendidas(self):
        for r in self:
            r.entradas_vendidas = len(r.entradas_ids)
    
    @api.depends('recinto_id.capacidad', 'entradas_vendidas')
    def _compute_entradas_disponibles(self):
        for r in self:
            r.entradas_disponibles = r.recinto_id.capacidad - r.entradas_vendidas

        