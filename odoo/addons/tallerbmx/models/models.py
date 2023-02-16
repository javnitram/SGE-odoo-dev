# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Bicicleta(models.Model):
    _name = 'tallerbmx.bicicleta'
    _description = 'Bicicletas'
    bicicleta_id = fields.Integer('id', required=True, help='Es obligatorio introducir el id')
    name = fields.Char('Nombre', help='Es obligatorio indicar la marca de la bicicleta') #campo obligatorio, y la ayuda lo mostrar como etiqueta flotante
    cliente_id = fields.Many2one('tallerbmx.cliente', string='Dueño de las bicis')
    empleado_ids = fields.Many2many('tallerbmx.empleado', string='Empleados')    
    categoria = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='Categorias')

class Empleado(models.Model):
   _name = 'tallerbmx.empleado'
   _description = 'Lista empleados'
   empleado_id = fields.Integer('id')
   name = fields.Char('Nombre')
   bicicleta_ids = fields.Many2many('tallerbmx.bicicleta', string='Bicicleta')

class Pieza(models.Model):
   _name = 'tallerbmx.pieza'
   _description = 'Piezas disponibles para reparar'
   pieza_id = fields.Integer('id')
   name = fields.Char('Nombre')
   tipo = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='Tipos de pieza')

class Cliente(models.Model):
   _name = 'tallerbmx.cliente'
   _description = 'Lista de clientes'
   cliente_id = fields.Integer('id')
   name = fields.Char('Nombre')
   apellido = fields.Char('Apellido')
   bicicletas_ids = fields.One2many('tallerbmx.bicicleta', 'bicicleta_id', string='Bicicletas del cliente')
    
# class tallerbmx(models.Model):
#     _name = 'tallerbmx.tallerbmx'
#     _description = 'tallerbmx.tallerbmx'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
