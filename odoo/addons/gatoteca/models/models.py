# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GatotecaEmpleado(models.Model):
    _name = 'gatoteca.empleado'
    _description = 'Empleados'
    name = fields.Char('Empleado',required=True)

class GatotecaJefe(models.Model):
    _name = 'gatoteca.jefe'
    _description = 'Jefe'
    name = fields.Char('Jefe',required=True)

class GatotecaCliente(models.Model):
    _name = 'gatoteca.cliente'
    _description = 'Cliente'
    name = fields.Char('Cliente',required=True)

class GatotecaGato(models.Model):
    _name = 'gatoteca.gato'
    _description = 'Gato'
    name = fields.Char('Gato',required=True)
    raza = fields.Selection([
        ('0', 'Siames'),
        ('1', 'Sphynx'),
        ('2', 'Persa'),
        ('3', 'scottish fold'),
        ('4', 'Comun europeo')
    ], string='raza')
    
    
    
    

# class gatoteca(models.Model):
#     _name = 'gatoteca.gatoteca'
#     _description = 'gatoteca.gatoteca'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
