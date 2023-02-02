# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TallerVehiculos(models.Model):
   _name = 'ig.taller.vehiculos'
   _description = 'Taller.vehiculos'
   name=fields.Char('marca',required=True)
   matricula=fields.Char('matricula',required=True)
   
class TallerRecambios(models.Model):
   _name = 'ig.taller.recambios'
   _description = 'Taller.Recambios'
   name=fields.Char('pieza',required=True)
   cantidad=fields.Integer('cantidad',required=True)

class TallerClientes(models.Model):
   _name = 'ig.taller.clientes'
   _description = 'Taller.Clientes'
   name=fields.Char('nombre',required=True)
   dni=fields.Char('dni',required=True,default='hola')


class TallerProveedores(models.Model):
   _name = 'ig.taller.proveedores'
   _description = 'Taller.Proveedores'
   name=fields.Char('Nombre Empresa',required=True)
   
   
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
