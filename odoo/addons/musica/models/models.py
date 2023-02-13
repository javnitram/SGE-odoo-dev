# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TiendainstrumentosCategoria(models.Model):
    _name = 'jr.tiendainstrumento.categoria'
    _description = 'model.technical.name'
    name = fields.Char('Nombre', required=True)
    instrumento_id = fields.One2many('jr.tiendainstrumento.instrumento', 'categoria_id', string='Instrumentos por categoria')

class TiendainstrumentosInstrumento(models.Model):
    _name = 'jr.tiendainstrumento.instrumento'
    _description = 'model.technical.name'
    modelo = fields.Char('Modelo')
    precio = fields.Float('Precio',required=True)
    marca = fields.Char('Marca', required=True)
    stock = fields.Float('Stock')
    fecha = fields.Date('Fecha')
    categoria_id = fields.Many2one('jr.tiendainstrumento.categoria', string='Categoria')
    venta_id = fields.Many2one('jr.tiendainstrumento.venta', string='Venta')


class TiendainstrumentosVenta(models.Model):
    _name = 'jr.tiendainstrumento.venta'
    _description = 'model.technical.name'
    fecha = fields.Date('fecha')
    precioPedido = fields.Float('Precio', required=True)
    numeroProductos = fields.Char('Numero de productos', required=True)

    
class TiendainstrumentosCliente(models.Model):
    _name = 'jr.tiendainstrumento.cliente'
    _description = 'model.technical.name'
    nombreCliente = fields.Char('Nombre', required=True)
    dni = fields.Char('dni', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
   
#oofon


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
