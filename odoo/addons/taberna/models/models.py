# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TabernaInformacion(models.Model):
    _name = 'jm.taberna.informacion'
    _description = 'jm.taberna.informacion'
    nombre = fields.Char('nombre', required=True)
    direccion = fields.Char('direccion', required=True)
    id_empleado = fields.Integer('id_empleado', required=True)

class TabernaBebidas(models.Model):
    _name = 'jm.taberna.bebidas'
    _description = 'jm.taberna.bebidas'
    id_bebida = fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    alcohol = fields.Boolean('alcohol', required=True)
    tipo = fields.Char('tipo', required=True)
    pais = fields.Char('pais', required=True)
    tipo = fields.Selection([
        ('1', 'rubia'),
        ('2', 'tostada'),
        ('3', 'negra')
    ], string='tipo')

class TabernaEmpleados(models.Model):
    _name = 'jm.taberna.empleados'
    _description = 'jm.taberna.empleados'
    id_empleado = fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    apellido1 = fields.Char('apellido1', required=True)
    apellido2 = fields.Char('apellido2')
    salario = fields.Float('salario')
    telefono = fields.Integer('telefono', required=True)
    categoria = fields.Selection([
        ('1', 'camarero'),
        ('2', 'cocinero'),
    ], string='categoria')

class TabernaClientes(models.Model):
    _name = 'jm.taberna.clientes'
    _description = 'jm.taberna.clientes'
    id_cliente= fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    apellido1 = fields.Char('apellido1', required=True)
    apellido2 = fields.Char('apellido2')

class TabernaPedidos(models.Model):
    _name = 'jm.taberna.pedidos'
    _description = 'jm.taberna.pedidos'
    id_pedidos = fields.Integer('id', required=True)
    cantidad = fields.Integer('cantidad', required=True)
    id_bebida = fields.Integer('id', required=True)
    id_empleado = fields.Integer('id', required=True)
    id_empleado = fields.Integer('id', required=True)
    id_cliente= fields.Integer('id', required=True)

# classpaisuired
# salario = fields.Float('salario')=Truern, re, requ, required=Trueired=Trueq
# tipo = fields.Char('tipo', required=True)uired=Truea(models., required=TrueModel):
#     _name = 'taberna.taberna'
#     _description = 'taberna.taberna'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
