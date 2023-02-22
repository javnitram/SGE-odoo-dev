# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TiendainstrumentosCategoria(models.Model):
    _name = 'jr.tiendainstrumento.categoria'
    _description = 'model.technical.name'
    name = fields.Char('Nombre', required=True)
    instrumento_id = fields.One2many('jr.tiendainstrumento.instrumento', 'categoria_id',  string='Instrumentos por categoria')


class TiendainstrumentosInstrumento(models.Model):
    _name = 'jr.tiendainstrumento.instrumento'
    _description = 'model.technical.name'
    name = fields.Char('Modelo')
    precio = fields.Float('Precio',required=True)
    marca = fields.Char('Marca', required=True)
    stock = fields.Float('Stock')
    imagen = fields.Image(string="Imagen",store=True,relation="res.partner",help="Seleccionar imagen aquí")
    segundamano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
        ('0', 'Recien Fabricado'),('1', 'Casi Nuevo'), ('2', 'Algo Desgastado')
    ], string='estado', default = "0")

    categoria_id = fields.Many2one('jr.tiendainstrumento.categoria', string='Categoria')
    #ventas_ids = fields.Many2many('jr.tiendainstrumento.venta', string='Ventas')


class TiendainstrumentosVenta(models.Model):
    _name = 'jr.tiendainstrumento.venta'
    _description = 'model.technical.name'
    fecha = fields.Date('fecha')
    #cliente_id = fields.Many2one('jr.tiendainstrumento.cliente', string='Cliente')
    #clientes_ids = fields.Many2many('jr.tiendainstrumento.cliente','ventas_ids', string='Clientes')
    instrumentos_ids = fields.Many2many('jr.tiendainstrumento.instrumento', string='Instrumentos')
    cliente_id = fields.Many2one('jr.tiendainstrumento.cliente', string='Cliente')


class TiendainstrumentosCliente(models.Model):
    _name = 'jr.tiendainstrumento.cliente'
    _description = 'model.technical.name'
    nombreCliente = fields.Char('Nombre', required=True)
    dni = fields.Char('dni', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    phone = fields.Integer('Phone')
    ventas_ids = fields.One2many('jr.tiendainstrumento.venta', 'cliente_id', string='Compras')
    #ventas_ids = fields.One2many('jr.tiendainstrumento.venta', 'cliente_id', string='Pedidos realizados')
    #ventas_ids = fields.Many2many('jr.tiendainstrumento.venta', 'clientes_ids',  string='Ventas')
   
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
