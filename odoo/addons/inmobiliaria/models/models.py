# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InmobiliariaInmueble(models.Model):
    _name = 'il.inmobiliaria.inmueble'
    _description = 'il.inmobiliaria.inmueble'
    referencia = fields.Char('Referencia',required=True)
    nombre = fields.Char('Nombre',help='Introduce el nombre del inmueble')
    tipo = fields.Selection([
        ('0', 'Piso'),('1', 'Casa'),('2', 'Chalet'),('3', 'Local'),('4', 'Terreno urbano')
    ], string='Tipo')
    #Precio
    #m2
    fecha_entrada = fields.Date('Fecha_entrada')


class InmobiliariaCiente(models.Model):
    _name = 'il.inmobiliaria.cliente'
    _description = 'il.inmobiliaria.cliente'
    id_cliente = fields.Integer('Id_cliente')
    nombre = fields.Char('Nombre')
    apellido1 = fields.Char('Primer apellido')
    apellido2 = fields.Char('Segundo apellido')

class InmobiliariaAgente(models.Model):
    _name = 'il.inmobiliaria.agente'
    _description = 'il.inmobiliaria.agente'
    id_agente = fields.Integer('Id_agente')
    nombre = fields.Char('Nombre')
    apellido1 = fields.Char('Primer apellido')
    apellido2 = fields.Char('Segundo apellido')
    puesto = fields.Selection([
        ('0', 'Agente inmobiliario'),('1', 'Director')
    ], string='Puesto')
    #Salario

class InmobiliariaVenta(models.Model):
    _name = 'il.inmobiliaria.venta'
    _description = 'il.inmobiliaria.venta'
    Id_venta = fields.Char('Id_venta',required=True)
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
