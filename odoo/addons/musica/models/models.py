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
    ], string='Estado', default = "0")
    ventas_ids = fields.Many2many('jr.tiendainstrumento.venta', string='Instrumentos vendidos')
    categoria_id = fields.Many2one('jr.tiendainstrumento.categoria', string='Categoria')
    

class TiendainstrumentosVenta(models.Model):
    _name = 'jr.tiendainstrumento.venta'
    _description = 'model.technical.name'
    fecha = fields.Date('fecha')
    instrumentos_ids = fields.Many2many('jr.tiendainstrumento.instrumento', string='Instrumentos')
    cliente_id = fields.Many2one('jr.tiendainstrumento.cliente', string='Cliente')


class TiendainstrumentosCliente(models.Model):
    _name = 'jr.tiendainstrumento.cliente'
    _description = 'model.technical.name'
    name = fields.Char('Nombre y Apellidos', required=True)
    dni = fields.Char('dni', required=True)
    fecha_nacimiento = fields.Date('Fecha de nacimiento')
    phone = fields.Integer('Phone')
    ventas_ids = fields.One2many('jr.tiendainstrumento.venta', 'cliente_id', string='Compras')
    
