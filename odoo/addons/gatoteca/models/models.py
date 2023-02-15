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
    tipo = fields.Selection([
        ('0', 'Desayuno'),
        ('1','Comida'),
        ('2','Merienda'),
        ('3','Solo bebida')
    ], string='Tipo',required=True)
    precio = fields.Integer('Precio')

class GatotecaCliente(models.Model):
    _name = 'gatoteca.cliente'
    _description = 'Cliente'
    name = fields.Char('Cliente',required=True)
    email = fields.Char('Email')
    adopcion = fields.Boolean('Quiere adoptar')

class GatotecaGato(models.Model):
    _name = 'gatoteca.gato'
    _description = 'Gato'
    name = fields.Char('Gato',required=True)
    adopcion = fields.Boolean('Espera adopcion')

class GatotecaRaza(models.Model):
    _name = 'gatoteca.raza'
    _description = 'Registro de razas de gatos'
    name = fields.Char('Raza')
    existe = fields.Boolean('Se encuentra')
    


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
