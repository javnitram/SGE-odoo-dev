# -*- coding: utf-8 -*-

from odoo import models, fields, api
 
class CocinaPlato(models.Model):
    _name = 'fr.cocina.plato'
    _description = 'Plato de cocina'
    name = fields.Char('Plato')
    precio = fields.Float('Precio')
    temperatura = fields.Selection([
        ('0', 'Frio'),
        ('1', 'Caliente')
    ], string='Temperatura')
    partida_responsable_id = fields.Many2one('fr.cocina.partida', string='Partida Responsable')
    imagen = fields.Image('Imagen del Plato', max_width=200, max_height=200)

class CocinaPartida(models.Model):
    _name = 'fr.cocina.partida'
    _description = 'Partida de cocina'
    name = fields.Char('Partida')
    integrantes = fields.Integer('Numero de integrantes')
    descripcion = fields.Selection([
        ('0', 'Salado'),
        ('1', 'Dulce')
    ], string='Descripcion')
    platos_creados_ids = fields.One2many('fr.cocina.plato', 'partida_responsable_id', string='Platos creados')
    jefe_partida_id = fields.Many2one('fr.cocina.jefe', string='Jefe de partida')
    cliente_servido_ids = fields.Many2many('fr.cocina.cliente', string='Cliente servido')

class CocinaJefe(models.Model):
    _name = 'fr.cocina.jefe'
    _description = 'Jefe de cocina'
    name = fields.Char('Jefe')
    partida_manejada_ids = fields.One2many('fr.cocina.partida', 'jefe_partida_id', string='Partida controlada')
    

class CocinaCliente(models.Model):
    _name = 'fr.cocina.cliente'
    _description = 'Clientes del restaurante'
    name = fields.Char('Cliente')
    turno = fields.Selection([
        ('0', 'Comida'),
        ('1', 'Cena')
    ], string='Turno')
    partida_implicada_ids = fields.Many2many('fr.cocina.partida', string='Partida implicada')

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
