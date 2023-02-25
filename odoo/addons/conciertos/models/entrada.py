# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConciertosEntrada(models.Model):
    _name = 'sa.conciertos.entrada'
    _description = 'sa.conciertos.entrada'
    concierto_id = fields.Many2one('sa.conciertos.concierto', string='Concierto')
    num_entrada = fields.Integer(compute='_compute_num_entrada', string='Número de entrada', store=True)
    cliente_id = fields.Many2one('sa.conciertos.cliente', string='Cliente')
    zona = fields.Selection([
        ('1', 'Pista'),
        ('2', 'Grada lateral - 1a planta'),
        ('3', 'Grada lateral - 2a planta'),
        ('4', 'Grada trasera - 1a planta'),
        ('5', 'Grada trasera - 2a planta'),
    ], string='Zona')
    precio = fields.Float(compute='_compute_precio', string='Precio')
    
    @api.depends('concierto_id.entradas_ids')
    def _compute_num_entrada(self):
        for r in self:
            contador = 0
            for entrada in r.concierto_id.entradas_ids:
                contador += 1
                entrada.num_entrada = contador
        
    @api.depends('concierto_id', 'zona')
    def _compute_precio(self):
        for r in self:
            r.precio = r.concierto_id.precio_base
            if r.zona == '1':
                r.precio *= 1.8
            elif r.zona == '2':
                r.precio *= 1.6
            elif r.zona == '3':
                r.precio *= 1.5
            elif r.zona == '4':
                r.precio *= 1.4
            elif r.zona == '5':
                r.precio *= 1.2

    @api.constrains('concierto_id')
    def _constrains_concierto_id(self):
        for r in self:
            if len(r.concierto_id.entradas_ids) > r.concierto_id.recinto_id.capacidad:
                raise ValidationError("No quedan entradas disponibles para ese concierto")

    