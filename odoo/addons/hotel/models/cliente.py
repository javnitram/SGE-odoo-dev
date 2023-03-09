from odoo import models, fields, api
import datetime

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