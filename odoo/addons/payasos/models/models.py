# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payasos(models.Model):
    _name = 'dg.payasos'
    _description = 'dg.payasos'

    nombre = fields.Char('Nombre')
    edad = fields.Integer('Edad')
    color_nariz = fields.Char('Color de nariz')
    tarifa = fields.Integer('tarifa')
    #id_manager = fields.Many2one('dg.managers', string='id')

class managers(models.Model):
    _name = 'dg.managers'
    _description = 'dg.managers'

    nombre = fields.Char('Nombre')
    annos = fields.Integer('Años en la empresa')

class fiestas(models.Model):
    _name = 'dg.fiestas'
    _description = 'dg.fiestas'

    fecha = fields.Date('Fecha')
    direccion = fields.Char('Dirección')
    hora_comienzo = fields.Float('Hora de comienzo', compute="_compute_time")
    hora_fin = fields.Float('Hora de fin', compute="_compute_time")

class clientes(models.Model):
    _name = 'dg.clientes'
    _description = 'dg.clientes'

    nombre = fields.Char('Nombre')
    edad = fields.Integer('Edad')
    dni = fields.Char('DNI', required=True)
#
#  @api.depends('value')
#   def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
