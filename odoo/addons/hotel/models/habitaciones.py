from odoo import models, fields, api
import datetime

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