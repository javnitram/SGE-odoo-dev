# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConcesionarioPedidos(models.Model):
    _name = 'dhm.concesionario.pedidos'
    _description = 'Marcas'
    name = fields.Char('Nombre',required=True)
    descripcion = fields.Char('Descripcion')
    facturas_id = fields.Many2one('dhm.concesionario.facturas', string='Factura')
    clientes_id = fields.Many2one('dhm.concesionario.clientes', string='Clientes')

class ConcesionarioVehiculos(models.Model):
    _name = 'dhm.concesionario.vehiculos'
    _description = 'Vehiculo'
    name=fields.Char('Marca',required=True,help='Introduzca el nombre de la marca')
    modelo = fields.Char('Nombre',required=True,help='Introduzca el nombre del modelo')
    estado = fields.Selection([
        ('0', 'Nuevo'),
        ('1', 'KM-0'),
        ('2', 'Seminuevo'),
        ('3', 'Alquilado')
    ], string='Estado')
    imagen = fields.Image('Imagen')
    matricula = fields.Integer('Matricula',required=True)
    clientes_ids = fields.Many2many('dhm.concesionario.clientes', string='Clientes')

class ConcesionarioClientes(models.Model):
    _name = 'dhm.concesionario.clientes'
    _description = 'Clientes'
    name = fields.Char('Dni',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre')
    apellidos = fields.Char('Apellidos',required=True,help='Introduzca el apellido')
    pedidos_ids = fields.One2many('dhm.concesionario.pedidos', 'clientes_id', string='Pedidos')

class ConcesionarioFacturas(models.Model):
    _name = 'dhm.concesionario.facturas'
    _description = 'Facturas'
    name = fields.Char('Factura',required=True)
    cantidad = fields.Integer('Cantidad',required=True)
    precio = fields.Integer('Precio',required=True)  