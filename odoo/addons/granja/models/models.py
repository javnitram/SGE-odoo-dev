# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GranjaProducto(models.Model):
    _name = 'rh.granja.producto'
    _description = 'rh.granja.producto'
    name = fields.Char('NombreProdcuto',required=True,help='Introduce el nombre del producto')
    precio = fields.Integer('Precio/Kg',required=True,help='Introduce el precio por cada kilo del producto')
    description = fields.Text('Descripcion',help='Introduce la descripcion del producto')
    tipo = fields.Selection([
        ('animal', 'Animal'),
        ('vegetal', 'Vegetal'),
        ('hongo', 'Hongo')
    ], string='Tipo')
    imagen = fields.Image('Imagen',help='Introduce la imagen del producto')
    especie_ids = fields.Many2many('rh.granja.especie', string='Especie')
    

class GranjaCliente(models.Model):
    _name = 'rh.granja.cliente'
    _description = 'rh.granja.cliente'
    name = fields.Char('NombreCliente',required=True,help='Introduce el nombre del cliente')
    correo = fields.Char('Correo',help='Introduce el correo electronico del cliente')
    direccion = fields.Char('Direccion',help='Introduce la direccion del cliente')
    description = fields.Text('Descripcion',help='Introduce la descipcion del cliente')
    imagen = fields.Image('Imagen',help='Introduce la imagen del cliente')
    pedido_id = fields.One2many('rh.granja.pedido', 'cliente_ids', string='Pedido')


class GranjaEspecie(models.Model):
    _name = 'rh.granja.especie'
    _description = 'rh.granja.especie'
    name = fields.Char('NombreEspecie',required=True,help='Introduce el nombre común de la especie')
    nombre_cien = fields.Char('NombreCien',required=True,help='Introduce el nombre científico de la especie')
    description = fields.Text('Descripcion',help='Introduce la descripcion de la especie')
    imagen = fields.Image('Imagen',help='Introduce la imagen de la especie')

    
class GranjaPedido(models.Model):
    _name = 'rh.granja.pedido'
    _description = 'rh.granja.pedido'
    name = fields.Char('Nombre')
    fecha_entrega = fields.Date('FechaEntrega')
    description = fields.Text('Descripcion',help='Introduce la descipcion del cliente')
    cliente_ids = fields.Many2one('rh.granja.cliente', string='Cliente')
    producto_ids = fields.Many2many('rh.granja.producto', string='Producto')

