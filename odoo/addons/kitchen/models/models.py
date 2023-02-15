# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class CocinaPlato(models.Model):
    _name = 'cocina.plato'
    _description = 'Plato de cocina'
    name = fields.Char('Plato')
    precio = fields.Float('Precio')
    temperatura = fields.Selection([
        ('0', 'Frio'),
        ('1', 'Caliente')
    ], string='Temperatura')

class CocinaPartida(models.Model):
    _name = 'cocina.partida'
    _description = 'Partida de cocina'
    name = fields.Char('Partida')
    integrantes = fields.Integer('Numero de integrantes')
    descripcion = fields.Selection([
        ('0', 'Salado'),
        ('1', 'Dulce')
    ], string='Descripcion')

class CocinaJefe(models.Model):
    _name = 'cocina.jefe'
    _description = 'Jefe de cocina'
    name = fields.Char('Jefe')
    partida = fields.Char('Partida')

class CocinaCliente(models.Model):
    _name = 'cocina.cliente'
    _description = 'Clientes del restaurante'
    name = fields.Char('Cliente')
    turno = fields.Selection([
        ('0', 'Comida'),
        ('1', 'Cena')
    ], string='Turno')

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
