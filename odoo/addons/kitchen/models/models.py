# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class CocinaPlato(models.Model):
    _name = 'cocina.plato'
    _description = 'Plato de cocina'
    name = fields.Char('Plato')
    precio = fields.Float('Precio')
    temperatura = fields.Selection([
        ('0', 'frio'),
        ('1', 'caliente')
    ], string='Temperatura')

class CocinaPartida(models.Model):
    _name = 'cocina.partida'
    _description = 'Partida de cocina'
    name = fields.Char('Partida')

class CocinaJefe(models.Model):
    _name = 'cocina.jefe'
    _description = 'Jefe de cocina'
    name = fields.Char('Jefe')

class CocinaCliente(models.Model):
    _name = 'cocina.cliente'
    _description = 'Clientes del restaurante'
    name = fields.Char('Cliente')

# class kitchen(models.Model):
#     _name = 'kitchen.kitchen'
#     _description = 'kitchen.kitchen'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
