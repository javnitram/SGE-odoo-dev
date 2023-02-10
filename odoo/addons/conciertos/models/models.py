# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosArtista(models.Model):
    _name = 'sa.conciertos.artista'
    _description = 'sa.conciertos.artista'
    nombre = fields.Char('Nombre', required=True)

class ConciertoRecinto(models.Model):
    _name = 'sa.conciertos.recinto'
    _description = 'sa.conciertos.recinto'
    nombre = fields.Char('Nombre')
    ciudad = fields.Char('Ciudad')
    pais = fields.Selection([
        ('key', 'value')
    ], string='País')
    capacidad = fields.Integer('Capacidad')

class ConciertosConcierto(models.Model):
    _name = 'sa.conciertos.concierto'
    _description = 'sa.conciertos.concierto'
    fecha = fields.Date('Fecha')
    artista_id = fields.Many2one('sa.conciertos.artista', string='Artista')
    recinto_id = fields.Many2one('sa.conciertos.recinto', string='Recinto', help='El recinto donde tendrá lugar')
    

class ConciertoEntrada(models.Model):
    _name = 'sa.conciertos.entrada'
    _description = 'sa.conciertos.entrada'
    concierto_id = fields.Many2one('sa.conciertos.concierto', string='Concierto')
    precio = fields.Float('Precio')

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
