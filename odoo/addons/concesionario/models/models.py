# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConcesionarioPedidos(models.Model):
    _name = 'dhm.concesionario.pedidos'
    _description = 'Marcas'
    nombre = fields.Char('Nombre',required=True)
    descripcion = fields.Char('Descripcion')
    vehiculos_ids = fields.One2many('dhm.concesionario.vehiculos', 'vehiculos_id', string='vehiculos')

class ConcesionarioVehiculos(models.Model):
    _name = 'dhm.concesionario.vehiculos'
    _description = 'Vehiculo'
    marca = fields.Char('Nombre',required=True,help='Introduzca el nombre de la marca')
    modelo = fields.Char('Nombre',required=True,help='Introduzca el nombre del modelo')
    estado = fields.Selection([
        ('0', 'Nuevo'),
        ('1', 'KM-0'),
        ('2', 'Seminuevo')
    ], string='Estado')
    matricula = fields.Integer('Matricula',required=True)
    vehiculos_id = fields.Many2one('dhm.concesionario.vehiculos', string='vehiculos')

class ConcesionarioClientes(models.Model):
    _name = 'dhm.concesionario.clientes'
    _description = 'Clientes'
    dni = fields.Integer('Dni',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre')
    apellidos = fields.Char('Apellidos',required=True,help='Introduzca el apellido')


class ConcesionarioFacturas(models.Model):
    _name = 'dhm.concesionario.facturas'
    _description = 'Facturas'
    cantidad = fields.Integer('Cantidad',required=True)
    precio = fields.Integer('Precio',required=True)
    