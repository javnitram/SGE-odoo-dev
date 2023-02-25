# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConciertosEntrada(models.Model):
    _name = 'sa.conciertos.entrada'
    _description = 'sa.conciertos.entrada'
    concierto_id = fields.Many2one('sa.conciertos.concierto', string='Concierto', required=True)
    cliente_id = fields.Many2one('sa.conciertos.cliente', string='Cliente', required=True)
    zona = fields.Selection([
        ('0', 'Pista'),
        ('1', 'Grada lateral - 1a planta'),
        ('2', 'Grada lateral - 2a planta'),
        ('3', 'Grada trasera - 1a planta'),
        ('4', 'Grada trasera - 2a planta'),
    ], string='Zona', required=True)

    # Campos calculados
    num_entrada = fields.Integer(compute='_compute_num_entrada', string='Número de entrada', store=True)
    currency_id = fields.Many2one('res.currency', compute='_compute_currency_id', string='Divisa')
    precio = fields.Monetary(compute='_compute_precio', string='Precio')
    name = fields.Char(compute='_compute_name', string='Nombre')
    
    @api.depends('concierto_id','num_entrada')
    def _compute_name(self):
        for r in self:
            r.name = r.concierto_id.name + " nº " + str(r.num_entrada)

    @api.depends('concierto_id.entradas_ids')
    def _compute_num_entrada(self):
        for r in self:
            contador = 0
            for entrada in r.concierto_id.entradas_ids:
                contador += 1
                entrada.num_entrada = contador
    
    @api.depends('concierto_id.currency_id')
    def _compute_currency_id(self):
        for r in self:
            r.currency_id = r.concierto_id.currency_id
        
    @api.depends('concierto_id', 'zona')
    def _compute_precio(self):
        for r in self:
            r.precio = r.concierto_id.precio_base
            if r.zona == '0':
                r.precio *= 1.8
            elif r.zona == '1':
                r.precio *= 1.6
            elif r.zona == '2':
                r.precio *= 1.5
            elif r.zona == '3':
                r.precio *= 1.4
            elif r.zona == '4':
                r.precio *= 1.2

    @api.constrains('concierto_id')
    def _constrains_concierto_id(self):
        for r in self:
            if len(r.concierto_id.entradas_ids) > r.concierto_id.recinto_id.capacidad:
                raise ValidationError("No quedan entradas disponibles para ese concierto")

    