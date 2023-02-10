# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TabernaInformacion(models.Model):
    _name = 'jm.taberna.informacion'
    _description = 'jm.taberna.informacion'
    nombre = fields.Char('nombre', required=True)
    direccion = fields.Char('direccion')

class TabernaBebidas(models.Model):
    _name = 'jm.taberna.bebidas'
    _description = 'jm.taberna.bebidas'
    id_bebida = fields.Integer('id', required=True)
    nombre = fields.Char('nombre')
    alcohol = fields.Boolean('alcohol')
    tipo = fields.Char('tipo')
    pais = fields.Char('pais')
    tipo = fields.Selection([
        ('1', 'rubia'),
        ('2', 'tostada'),
        ('3', 'negra')
    ], string='tipo')
    id_pedidos = fields.Many2many('jm.taberna.pedidos', string='id_pedidos')

class TabernaEmpleados(models.Model):
    _name = 'jm.taberna.empleados'
    _description = 'jm.taberna.empleados'
    id_empleado = fields.Integer('id', required=True)
    nombre = fields.Char('nombre')
    apellido1 = fields.Char('apellido1')
    apellido2 = fields.Char('apellido2')
    salario = fields.Float('salario')
    telefono = fields.Integer('telefono')
    categoria = fields.Selection([
        ('1', 'camarero'),
        ('2', 'cocinero'),
    ], string='categoria')
    nombre_taberna = fields.Many2one('jm.taberna.informacion', string='nombre_taberna')

class TabernaClientes(models.Model):
    _name = 'jm.taberna.clientes'
    _description = 'jm.taberna.clientes'
    id_cliente= fields.Integer('id', required=True)
    nombre = fields.Char('nombre')
    apellido1 = fields.Char('apellido1')
    apellido2 = fields.Char('apellido2')

class TabernaPedidos(models.Model):
    _name = 'jm.taberna.pedidos'
    _description = 'jm.taberna.pedidos'
    id_pedidos = fields.Integer('id', required=True)
    cantidad = fields.Integer('cantidad')
    id_empleado = fields.Many2one('jm.taberna.empleados', string='id_empleado')
    id_cliente = fields.Many2one('jm.taberna.clientes', string='id_cliente')
    id_bebida = fields.Many2many('jm.taberna.bebidas', string='id_bebida')

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
