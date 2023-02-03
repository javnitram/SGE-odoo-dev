# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TiendainstrumentosCategoria(models.Model):
    _name = 'jr.tiendainstrumento.categoria'
    _description = 'model.technical.name'
    name = fields.Char('Nombre', required=True)

class TiendainstrumentosInstrumento(models.Model):
    _name = 'jr.tiendainstrumento.instrumento'
    _description = 'model.technical.name'
    modelo = fields.Char('Modelo')
    precio = fields.Float('Precio',required=True)
    marca = fields.Char('Marca', required=True)
    stock = fields.Float('Stock')
    fecha = fields.Date('Fecha')


class TiendainstrumentosVenta(models.Model):
    _name = 'jr.tiendainstrumento.venta'
    _description = 'model.technical.name'
    fecha = fields.Date('fecha')
    precioPedido = fields.Float('Precio', required=True)
    numeroProductos = fields.Char('Numero de productos', required=True)
    


# class musica(models.Model):
#     _name = 'musica.musica'
#     _description = 'musica.musica'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
