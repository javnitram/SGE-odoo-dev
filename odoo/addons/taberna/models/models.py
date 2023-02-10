# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TabernaInformacion(models.Model):
    _name = 'jm.taberna.informacion'
    _description = 'jm.taberna.informacion'
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección')

class TabernaBebidas(models.Model):
    _name = 'jm.taberna.bebidas'
    _description = 'jm.taberna.bebidas'
    id_bebida = fields.Integer('ID', required=True)
    nombre = fields.Char('Nombre')
    alcohol = fields.Boolean('Alcohol')
    pais = fields.Char('Pais')
    tipo = fields.Selection([
        ('1', 'Rubia'),
        ('2', 'Tostada'),
        ('3', 'Negra')
    ], string='Tipo')
    id_pedidos = fields.Many2many('jm.taberna.pedidos', string='id_pedidos')

class TabernaEmpleados(models.Model):
    _name = 'jm.taberna.empleados'
    _description = 'jm.taberna.empleados'
    id_empleado = fields.Integer('ID', required=True)
    nombre = fields.Char('Nombre')
    apellido1 = fields.Char('Apellido 1')
    apellido2 = fields.Char('Apellido 2')
    salario = fields.Float('Salario')
    telefono = fields.Integer('Teléfono')
    categoria = fields.Selection([
        ('1', 'Camarero'),
        ('2', 'Cocinero'),
    ], string='Categoría')
    nombre_taberna = fields.Many2one('jm.taberna.informacion', string='Nombre de la taberna')

class TabernaClientes(models.Model):
    _name = 'jm.taberna.clientes'
    _description = 'jm.taberna.clientes'
    id_cliente= fields.Integer('ID', required=True)
    nombre = fields.Char('Nombre')
    apellido1 = fields.Char('Apellido 1')
    apellido2 = fields.Char('Apellido 2')

class TabernaPedidos(models.Model):
    _name = 'jm.taberna.pedidos'
    _description = 'jm.taberna.pedidos'
    id_pedidos = fields.Integer('ID', required=True)
    cantidad = fields.Integer('Cantidad')
    id_empleado = fields.Many2one('jm.taberna.empleados', string='ID de empleado')
    id_cliente = fields.Many2one('jm.taberna.clientes', string='ID de cliente')
    id_bebida = fields.Many2many('jm.taberna.bebidas', string='ID de bebida')

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
