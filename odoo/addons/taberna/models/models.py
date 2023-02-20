# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TabernaInformacion(models.Model):
    _name = 'jm.taberna.informacion'
    _description = 'jm.taberna.informacion'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Imagen")
    name = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección')
    empleado_ids = fields.One2many('jm.taberna.empleados', 'id_empleado', string='ID del empleado')

class TabernaBebidas(models.Model):
    _name = 'jm.taberna.bebidas'
    _description = 'jm.taberna.bebidas'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Imagen")
    id_bebida = fields.Integer('ID', required=True)
    name = fields.Char('Nombre')
    alcohol = fields.Boolean('Alcohol')
    tipo = fields.Selection([
        ('1', 'Rubia'),
        ('2', 'Tostada'),
        ('3', 'Negra')
    ], string='Tipo')
    precio = fields.Integer('Precio', required=True)
    id_pedidos = fields.Many2many('jm.taberna.pedidos', string='id_pedidos')
    pais_id = fields.Many2one('res.country', string='País')

class TabernaEmpleados(models.Model):
    _name = 'jm.taberna.empleados'
    _description = 'jm.taberna.empleados'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Imagen")
    id_empleado = fields.Integer('ID', required=True)
    name = fields.Char('Nombre')
    apellido1 = fields.Char('Apellido 1')
    apellido2 = fields.Char('Apellido 2')
    salario = fields.Float('Salario')
    telefono = fields.Integer('Teléfono')
    categoria = fields.Selection([
        ('1', 'Camarero'),
        ('2', 'Cocinero'),
    ], string='Categoría')
    nombre_taberna = fields.Many2one('jm.taberna.informacion', string='Nombre de la taberna')
    pedidos_ids = fields.One2many('jm.taberna.pedidos', 'id_pedidos', string='ID de pedido')

class TabernaClientes(models.Model):
    _name = 'jm.taberna.clientes'
    _description = 'jm.taberna.clientes'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Imagen")
    id_cliente= fields.Integer('ID', required=True)
    name = fields.Char('Nombre')
    apellido1 = fields.Char('Apellido 1')
    apellido2 = fields.Char('Apellido 2')
    pedidos_ids = fields.One2many('jm.taberna.pedidos', 'id_pedidos', string='ID de pedido')

class TabernaPedidos(models.Model):
    _name = 'jm.taberna.pedidos'
    _description = 'jm.taberna.pedidos'
    id_pedidos = fields.Integer('ID', required=True)
    cantidad = fields.Integer('Cantidad:')
    #total_pedido = fields.Integer('Total pedido:')
    total_pedido = fields.Integer(string='Total pedido', compute='calcular_total_pedido', store=True)
    id_empleado = fields.Many2one('jm.taberna.empleados', string='ID de empleado')
    id_cliente = fields.Many2one('jm.taberna.clientes', string='ID de cliente')
    id_bebida = fields.Many2many('jm.taberna.bebidas', string='ID de bebida')

    @api.depends('precio','cantidad')

    def _calcular_total_pedido(self):
        for r in self:
            r.total_pedido = r.cantidad * r.precio

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
