# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelCliente(models.Model):
    _name = 'jf.hotel.cliente'
    _description = 'Modelo Cliente'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Selecciona imagen aquí")
    dni = fields.Integer(string='DNI',required=True)
    name = fields.Char(string='Nombre',required=True)
    apellidos = fields.Char(string='Apellidos',required=True)
    telefono = fields.Integer(string='Telefono',required=True)
    correo = fields.Char(string='Correo')
    empresa_id = fields.Many2one('jf.hotel.empresa', string='Empresa')
    reserva_ids = fields.One2many('jf.hotel.reserva', 'cliente_id', string='Reservas del cliente')

class HotelEmpresa(models.Model):
    _name = 'jf.hotel.empresa'
    _description = 'Modelo Empresa'
    imagen = fields.Image(string='Imagen',store=True,relation="res.partner",help="Selecciona imagen aquí")
    name = fields.Char(string='Nombre',required=True)
    telefono = fields.Integer(string='Teléfono',required=True)
    correo = fields.Char(string='Correo')
    sitio_web = fields.Char(string='Sitio Web')
    direccion = fields.Char(string='Dirección',required=True)
    localidad = fields.Char(string='Localidad',required=True)
    pais_id = fields.Many2one('res.country', string='Pais de la empresa')
    cliente_ids = fields.One2many('jf.hotel.cliente', 'empresa_id', string='Clientes de la empresa')

class HotelReserva(models.Model):
    _name = 'jf.hotel.reserva'
    _description = 'Modelo Reserva'
    name = fields.Integer(string='DNI del cliente',required=True)
    fecha_inicio = fields.Date(string='Fecha inicio reserva',required=True)
    fecha_final = fields.Date(string='Fecha final reserva',required=True)
    precio_total = fields.Float(string='Precio total',required=True)
    cliente_id = fields.Many2one('jf.hotel.cliente', string='Cliente')
    habitacion_ids = fields.Many2many('jf.hotel.habitaciones', string='Habitacion/es reservada/s')

class HotelHabitaciones(models.Model):
    _name = 'jf.hotel.habitaciones'
    _description = 'Modelo Habitaciones'
    name = fields.Integer(string='Número de la habitación', required=True)
    plazas = fields.Integer(string='Plazas',required=True)
    precio = fields.Float(string='Precio por noche',required=True)
    planta = fields.Integer(string='Planta',required=True)
    estado = fields.Selection([
        ('0','Disponible'),('1','Ocupado')
    ],string='Estado',default="0")
    reserva_ids = fields.Many2many('jf.hotel.reserva', string='Reservas de la habitación')
