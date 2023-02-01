# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InmobiliariaInmueble(models.Model):
    _name = 'il.inmobiliaria.inmueble'
    _description = 'il.inmobiliaria.inmueble'
    referencia = fields.Char('Referencia',required=True)
    nombre = fields.Char('Nombre',help='Introduce el nombre del inmueble')
    tipo = fields.Selection([
        ('0', 'Piso'),('1', 'Casa'),('2', 'Chalet'),('3', 'Local'),('4', 'Terreno urbano')
    ], string='tipo')
    #Precio

class InmobiliariaCiente(models.Model):
    _name = 'il.inmobiliaria.cliente'
    _description = 'il.inmobiliaria.cliente'

class InmobiliariaAgente(models.Model):
    _name = 'il.inmobiliaria.agente'
    _description = 'il.inmobiliaria.agente'

class InmobiliariaVenta(models.Model):
    _name = 'il.inmobiliaria.venta'
    _description = 'il.inmobiliaria.venta'
    referencia = fields.Char('Referencia',required=True)
    #Cliente relacion de clase cliente
    #Inmueble relacion de clase Inmueble
    #Agente relacion de clase Agente
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
