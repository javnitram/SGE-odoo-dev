# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Bicicleta(models.Model):
    _name = 'tallerbmx.bicicleta'
    _description = 'Bicicletas'
    idBicicleta = fields.Integer('idBicicleta', required=True, help='Es obligatorio introducir el id')
    nombre = fields.Char('nombre', required=True, help='Es obligatorio indicar la marca de la bicicleta') #campo obligatorio, y la ayuda lo mostrar como etiqueta flotante
    nroCliente = fields.Integer('nroCliente')
    categoria = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='categoria')

class Empleado(models.Model):
   _name = 'tallerbmx.empleado'
   _description = 'Lista empleados'
   nroEmpleado = fields.Integer('nroEmpleado')

class Reparacion(models.Model):
   _name = 'tallerbmx.reparacion'
   _description = 'Reparaciones en activo'
   idReparacion = fields.Integer('idReparacion')
   nroEmpleado = fields.Integer('nroEmpleado')
   nroPieza = fields.Integer('nroPieza')
   idBicicleta = fields.Integer('idBicicleta')
   informe = fields.Char('informe')

class Pieza(models.Model):
   _name = 'tallerbmx.pieza'
   _description = 'Piezas disponibles para reparar'
   nroPieza = fields.Integer('nroPieza')
   piezaBici = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='piezaBici')


class Cliente(models.Model):
   _name = 'tallerbmx.cliente'
   _description = 'Lista de clientes'
   nroCliente = fields.Integer('nroCliente')
   nombre = fields.Char('nombre')
   apellido = fields.Char('apellido')
    
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
