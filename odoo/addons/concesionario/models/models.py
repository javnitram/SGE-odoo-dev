# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConcesionarioPedidos(models.Model):
    _name = 'dhm.concesionario.pedidos'
    _description = 'Marcas'
    id = fields.Integer('Id',required=True)

class ConcesionarioVehiculos(models.Model):
    _name = 'dhm.concesionario.vehiculos'
    _description = 'Vehiculo'
    id = fields.Integer('Id',required=True)
    marca = fields.Char('Nombre',required=True,help='Introduzca el nombre de la marca')
    modelo = fields.Char('Nombre',required=True,help='Introduzca el nombre del modelo')
    estado = fields.Selection([
        ('0', 'Nuevo'),
        ('1', 'KM-0'),
        ('2', 'Seminuevo')
    ], string='Estado')

class ConcesionarioClientes(models.Model):
    _name = 'dhm.concesionario.clientes'
    _description = 'Clientes'
    dni = fields.Integer('Dni',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre')
    apellidos = fields.Char('apellidos',required=True,help='Introduzca el apellido')


class ConcesionarioMatriculacion(models.Model):
    _name = 'dhm.concesionario.matriculacion'
    _description = 'Matriculacion'
    matricula = fields.Integer('Matricula',required=True)
    
    