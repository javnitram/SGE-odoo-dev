# -*- coding: utf-8 -*-

from odoo import models, fields, api

#TABLAS
class VeterinariaMascotas(models.Model):
    _name = 'cm.veterinaria.mascotas'
    _description = 'veterinaria.mascotas'
    nombre = fields.Char('Nombre',required=True)
    race = fields.Char('Raza',required=True)
    owner = fields.Char('Owner')

class MascotasVacunas(models.Model):
    _name = 'cm.mascotas.vacunas'
    _description = 'mascotas.vacunas'
    vacuna = fields.Char('Vacuna', required=True)
    field_name = fields.Selection([
        ('0', 'Si'),
        ('1', 'Pendiente')
    ], string='Vacunado',required=True)
    #field_name_ids = fields.Many2many('comodel_name', string='field_name')

class VeterinariaVeterinario(models.Model):
    _name = 'cm.veterinaria.veterinario'
    _description = 'veterinaria.veterinario'
    nombre = fields.Char('Nombre',required=True)
    numemp = fields.Char('Num Empleado',required=True)

class VeterinariaCliente(models.Model):
    _name = 'cm.veterinaria.mascotascliente'
    _description = 'veterinaria.cliente'
    name = fields.Char('Nombre',required=True)
    field_name_ids = fields.One2many('comodel_name', 'inverse_field_name', string='field_name')

#class model.technical.name(models.Model):
 #   _name = 'model.technical.name'
  #  _description = 'model.technical.name'
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
