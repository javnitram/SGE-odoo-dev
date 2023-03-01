# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Bicicleta(models.Model):
    _name = 'ias.tallerbmx.bicicleta'
    _description = 'Bicicletas'
    name = fields.Char('Nombre', help='Es obligatorio indicar la marca de la bicicleta') #campo obligatorio, y la ayuda lo mostrar como etiqueta flotante
    cliente_id = fields.Many2one('ias.tallerbmx.cliente', string='Cliente')
    imagen = fields.Image(string="Foto de la bici",help="Seleccionar imagen aquí")
    categoria = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='Categorias')

class Empleado(models.Model):
   _name = 'ias.tallerbmx.empleado'
   _description = 'Lista empleados'
   name = fields.Char('Nombre')
   bicicleta_ids = fields.Many2many('ias.tallerbmx.bicicleta', string='Bicicletas')

class Pieza(models.Model):
   _name = 'ias.tallerbmx.pieza'
   _description = 'Piezas disponibles para reparar'
   name = fields.Char('Nombre')
   imagen = fields.Image(string="Foto de la pieza",help="Seleccionar imagen aquí")
   tipo = fields.Selection([
       ('0', 'Bmx'),
       ('1', 'Mountain'),
       ('2', 'Dirt')
   ], string='Tipos de pieza')

class Cliente(models.Model):
   _name = 'ias.tallerbmx.cliente'
   _description = 'Lista de clientes'
   name = fields.Char('Nombre')
   apellido = fields.Char('Apellido')
   bicicletas_ids = fields.One2many('ias.tallerbmx.bicicleta', 'cliente_id', string='Bicicletas')

   @api.constrains('name')
   def _check_name(self):
      letra = self.name[0]
      if letra != letra.upper():
         raise ValidationError("La primera letra debe estar en mayuscula")
