# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosArtista(models.Model):
    _name = 'sa.conciertos.artista'
    _description = 'sa.conciertos.artista'
    name = fields.Char('Nombre', required=True)
    conciertos_ids = fields.Many2many('sa.conciertos.concierto', string='Conciertos')
    foto = fields.Image('Foto', max_width=200, max_height=200)


class ConciertoRecinto(models.Model):
    _name = 'sa.conciertos.recinto'
    _description = 'sa.conciertos.recinto'
    name = fields.Char('Nombre')
    ciudad = fields.Char('Ciudad')
    pais_id = fields.Many2one('res.country', string='País')
    capacidad = fields.Integer('Capacidad')
    conciertos_ids = fields.One2many('sa.conciertos.concierto', 'recinto_id', string='Conciertos')
    

class ConciertosConcierto(models.Model):
    _name = 'sa.conciertos.concierto'
    _description = 'sa.conciertos.concierto'
    name = fields.Char('Nombre')
    fecha = fields.Date('Fecha')
    artistas_ids = fields.Many2many('sa.conciertos.artista', string='Artistas')
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
    

class ConciertosEntrada(models.Model):
    _name = 'sa.conciertos.entrada'
    _description = 'sa.conciertos.entrada'
    concierto_id = fields.Many2one('sa.conciertos.concierto', string='Concierto')
    cliente_id = fields.Many2one('sa.conciertos.cliente', string='Cliente')
    zona = fields.Selection([
        ('1', 'Pista'),
        ('2', 'Grada lateral - 1a planta'),
        ('3', 'Grada lateral - 2a planta'),
        ('4', 'Grada trasera - 1a planta'),
        ('5', 'Grada trasera - 2a planta'),
    ], string='Zona')
    precio = fields.Float(compute='_compute_precio', string='Precio')
    
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

    
class ConciertosCliente(models.Model):
    _name = 'sa.conciertos.cliente'
    _description = 'sa.conciertos.cliente'
    name = fields.Char('Nombre')
    email = fields.Char('Email')

    

# class conciertos(models.Model):
#     _name = 'conciertos.conciertos'
#     _description = 'conciertos.conciertos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
