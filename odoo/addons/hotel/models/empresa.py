from odoo import models, fields, api
import datetime

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