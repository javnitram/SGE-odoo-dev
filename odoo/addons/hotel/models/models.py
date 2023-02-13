# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HotelCliente(models.Model):
    _name = 'jf.hotel.cliente'
    _description = 'jf.hotel.cliente'
    dni = fields.Integer(string='DNI',required=True)
    nombre = fields.Char(string='Nombre',required=True)
    apellidos = fields.Char(string='Apellidos',required=True)
    telefono = fields.Integer(string='Telefono',required=True)
    correo = fields.Char(string='Correo')
    empresa_id = fields.Many2one('jf.hotel.empresa', string='Empresa')
    reserva_id = fields.Many2one('jf.hotel.reserva', string='Reserva')

class HotelEmpresa(models.Model):
    _name = 'jf.hotel.empresa'
    _description = 'jf.hotel.empresa'
    nombre = fields.Char(string='Nombre',required=True)
    telefono = fields.Integer(string='Teléfono',required=True)
    correo = fields.Char(string='Correo')
    sitio_web = fields.Char(string='Sitio Web')
    direccion = fields.Char(string='Dirección',required=True)
    localidad = fields.Char(string='Localidad',required=True)
    pais = fields.Char(string='País',required=True)
    cliente_ids = fields.One2many('jf.hotel.cliente', 'empresa_id', string='Clientes de la empresa')

class HotelReserva(models.Model):
    _name = 'jf.hotel.reserva'
    _description = 'jf.hotel.reserva'
    dni_cliente = fields.Integer(string='dni_cliente',required=True)
    fecha_inicio = fields.Date(string='Fecha inicio reserva',required=True)
    fecha_final = fields.Date(string='Fecha final reserva',required=True)
    precio_total = fields.Float(string='Precio total',required=True)
    cliente_ids = fields.One2many('jf.hotel.cliente', 'reserva_id', string='Reservas del cliente')
    habitacion_ids = fields.Many2many('jf.hotel.habitaciones', string='Habitacion/es reservada/s')

class HotelHabitaciones(models.Model):
    _name = 'jf.hotel.habitaciones'
    _description = 'jf.hotel.habitaciones'
    numero = fields.Integer(string='Número de la habitación', required=True)
    plazas = fields.Integer(string='Plazas',required=True)
    precio = fields.Float(string='Precio por noche',required=True)
    planta = fields.Integer(string='Planta',required=True)
    estado = fields.Selection([
        ('0','Disponible'),('1','Ocupado')
    ],string='Estado',default="0")
    reserva_ids = fields.Many2many('jf.hotel.reserva', string='Reservas de la habitación')
    
    
    


# class hotel(models.Model):
#     _name = 'hotel.hotel'
#     _description = 'hotel.hotel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
