# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TallerVehiculos(models.Model):
   _name = 'ig.taller.vehiculos'
   _description = 'Taller.vehiculos'
   name=fields.Char('marca',required=True)
   color=fields.Char('color',required=True)
   matricula=fields.Char('matricula',required=True)
   tipo = fields.Selection(selection=[('0', 'Coche'),('1', 'Moto'),('2', 'vehiculo agrario'),('3', 'camión')],string='tipo',default='0')
   cliente_id = fields.Many2one('ig.taller.clientes', string='cliente')
   recambios_ids = fields.Many2many('ig.taller.recambios', string='Recambios')
   image=fields.Image('Imagen')

class TallerRecambios(models.Model):
   _name = 'ig.taller.recambios'
   _description = 'Taller.Recambios'
   name=fields.Char('pieza',required=True)
   cantidad=fields.Integer('cantidad',required=True)
   estado = fields.Selection(selection=[('0', 'Nuevo'),('0', 'como nuevo'),('2', 'de desguace')],string='estado' ,required=True,default='0')
   proveedores_ids = fields.Many2many('ig.taller.proveedores', string='Proveedores')

class TallerClientes(models.Model):
   _name = 'ig.taller.clientes'
   _description = 'Taller.Clientes'
   name=fields.Char('nombre',required=True)
   dni=fields.Char('dni',required=True)
   telefono=fields.Char('telefono',required=True)
   Vehiculos_id = fields.One2many('ig.taller.vehiculos', 'cliente_id', string='Vehiculos_id ')

class TallerProveedores(models.Model):
   _name = 'ig.taller.proveedores'
   _description = 'Taller.Proveedores'
   name=fields.Char('Nombre Empresa',required=True)
   telefono=fields.Char('telefono',required=True)
   localidad=fields.Char('localidad',required=True)
   recambios_ids = fields.Many2many('ig.taller.recambios', string='Recambios')
   
# class taller(models.Model):
#     _name = 'taller.taller'
#     _description = 'taller.taller'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
