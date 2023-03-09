from odoo import models, fields, api
import datetime

class HotelReserva(models.Model):
    _name = 'jf.hotel.reserva'
    _description = 'Modelo Reserva'
    fecha_inicio = fields.Date(string='Fecha inicio reserva',required=True)
    fecha_final = fields.Date(string='Fecha final reserva',required=True)
    precio_total = fields.Float(string='Precio total',compute="_precio_total",store=True)
    cliente_id = fields.Many2one('jf.hotel.cliente', string='Cliente')
    habitacion_ids = fields.Many2many('jf.hotel.habitaciones', string='Habitacion/es reservada/s')

    @api.depends('fecha_inicio', 'fecha_final', 'habitacion_ids')
    def _precio_total(self):
        for i in self:
            for j in i.habitacion_ids:
                date1 = i.fecha_inicio.strftime("%Y-%m-%d")
                date2 = i.fecha_final.strftime("%Y-%m-%d")
                converted_date = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
                converted_date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
                diferencia_dias = (converted_date2 - converted_date).days
                i.precio_total = diferencia_dias*j.precio