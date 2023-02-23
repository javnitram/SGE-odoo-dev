# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GatotecaEmpleado(models.Model):
    _name = 'ss.gatoteca.empleado'
    _description = 'Empleado'
    name = fields.Char('Empleado',required=True)
    sueldo = fields.Integer('Sueldo')
    encargado = fields.Boolean('Encargado',required=True)
    puesto = fields.Selection([
        ('0', 'Dependiente'),
        ('1','Camarero')
    ], string='Puesto')

    gatos_ids = fields.Many2many('ss.gatoteca.gato', string='Gatos asignados')

class GatotecaCliente(models.Model):
    _name = 'ss.gatoteca.cliente'
    _description = 'Cliente'
    name = fields.Char('Cliente',required=True)
    email = fields.Char('Email')
    adopcion = fields.Boolean('Quiere adoptar')

    gatos_ids = fields.One2many('ss.gatoteca.gato', 'cliente_id', string='Gatos adoptados')

class GatotecaGato(models.Model):
    _name = 'ss.gatoteca.gato'
    _description = 'Gato'
    name = fields.Char('Nombre',required=True)
    imagen = fields.Image('Imagen del gato', max_width=200, max_height=200)

    empleados_ids = fields.Many2many('ss.gatoteca.empleado', string='Empleados asignados')
    cliente_id = fields.Many2one('ss.gatoteca.cliente', string='Adoptado por')
    raza_id = fields.Many2one('ss.gatoteca.raza', string='Raza')

class GatotecaRaza(models.Model):
    _name = 'ss.gatoteca.raza'
    _description = 'Registro de razas de gatos'
    name = fields.Char('Raza')
    procedencia = fields.Char('Procedencia')

    gatos_ids = fields.One2many('ss.gatoteca.gato', 'raza_id', string='Gatos')


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
