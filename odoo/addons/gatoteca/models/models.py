# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GatotecaEmpleado(models.Model):
    _name = 'gatoteca.empleado'
    _description = 'Empleado'
    name = fields.Char('Empleado',required=True)
    sueldo = fields.Integer('Sueldo')
    encargado = fields.Boolean('Encargado',required=True)
    puesto = fields.Selection([
        ('0', 'Dependiente'),
        ('1','Camarero')
    ], string='Puesto')

class GatotecaMenu(models.Model):
    _name = 'gatoteca.menu'
    _description = 'Menu'
    name = fields.Char('Menu',required=True)
    tipo = fields.Selection([
        ('0', 'Desayuno'),
        ('1','Comida'),
        ('2','Merienda'),
        ('3','Solo bebida')
    ], string='Tipo')
    precio = fields.Integer('Precio')

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
        ('3', 'Scottish fold'),
        ('4', 'Comun europeo')
    ], string='Raza')


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
