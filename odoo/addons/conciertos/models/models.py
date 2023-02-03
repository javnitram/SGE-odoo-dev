# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConciertosArtista(models.Model):
    _name = 'sa.conciertos.artista'
    _description = 'sa.conciertos.artista'
    nombre = fields.Char('nombre', required=True)

class ConciertoRecinto(models.Model):
    _name = 'sa.conciertos.recinto'
    _description = 'sa.conciertos.recinto'
    nombre = fields.Char('nombre')
    ciudad = fields.Char('ciudad')
    país = fields.Selection([
        ('key', 'value')
    ], string='país')
    capacidad = fields.Integer('capacidad')

class ConciertosConcierto(models.Model):
    _name = 'sa.conciertos.concierto'
    _description = 'sa.conciertos.concierto'
    fecha = fields.Date('fecha')
    artista_id = fields.Many2one('sa.conciertos.artista', string='artista')
    recinto_id = fields.Many2one('sa.conciertos.recinto', string='recinto')
    

class ConciertoEntrada(models.Model):
    _name = 'sa.conciertos.entrada'
    _description = 'sa.conciertos.entrada'
    precio = fields.Float('precio')


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
