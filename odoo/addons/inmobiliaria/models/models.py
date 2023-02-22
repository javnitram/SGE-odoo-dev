# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InmobiliariaInmueble(models.Model):
    _name = 'il.inmobiliaria.inmueble'
    _description = 'il.inmobiliaria.inmueble'

    imagen = fields.Image('imagen', store=True, relation="res.partner")
    name = fields.Char('Nombre',help='Introduce el nombre del inmueble')
    tipo = fields.Selection([
        ('0', 'Piso'),('1', 'Casa'),('2', 'Chalet'),('3', 'Local'),('4', 'Terreno urbano')
    ], string='Tipo')
    precio = fields.Float('Precio')
    m2 = fields.Float('m2')
    fecha_entrada = fields.Date('Fecha_entrada')
    venta_ids = fields.One2many('il.inmobiliaria.venta', 'inmueble_id', string='venta')

class InmobiliariaCiente(models.Model):
    _name = 'il.inmobiliaria.cliente'
    _description = 'il.inmobiliaria.cliente'

    name = fields.Char('Nombre')
    apellido1 = fields.Char('Primer apellido')
    apellido2 = fields.Char('Segundo apellido')
    venta = fields.Many2many('il.inmobiliaria.venta', string='cliente')

class InmobiliariaAgente(models.Model):
    _name = 'il.inmobiliaria.agente'
    _description = 'il.inmobiliaria.agente'

    name = fields.Char('Nombre')
    apellido1 = fields.Char('Primer apellido')
    apellido2 = fields.Char('Segundo apellido')
    puesto = fields.Selection([
        ('0', 'Agente inmobiliario'),('1', 'Director')
    ], string='Puesto')
    salario = fields.Float('Salario')
    venta_ids = fields.One2many('il.inmobiliaria.venta', 'agente', string='venta')

class InmobiliariaVenta(models.Model):
    _name = 'il.inmobiliaria.venta'
    _description = 'il.inmobiliaria.venta'

    cliente = fields.Many2many('il.inmobiliaria.cliente', string='cliente')
    inmueble_id = fields.Many2one('il.inmobiliaria.inmueble', string='inmueble')
    agente = fields.Many2one('il.inmobiliaria.agente', string='agente')
    fecha = fields.Date('Fecha')
    
    
    
    

# class inmobiliaria(models.Model):
#     _name = 'inmobiliaria.inmobiliaria'
#     _description = 'inmobiliaria.inmobiliaria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
