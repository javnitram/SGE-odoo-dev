# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payasos(models.Model):
    _name = 'dg.payasos.payasos'
    _description = 'dg.payasos.payasos'

    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripcion', help='Breve descripcion del payaso')
    edad = fields.Integer('Edad', required=True)
    color_nariz = fields.Selection([
        ('0', 'rojo'),
        ('1', 'verde'),
        ('2', 'azul celeste'),
        ('3', 'morado'),
        ('4', 'amarillo'),
        ('5', 'naranja'),
    ], string='Color de nariz', required=True, default=0)
    tarifa = fields.Float('tarifa', required=True)
    #id_manager = fields.Many2one('dg.managers', string='id')

class managers(models.Model):
    _name = 'dg.payasos.managers'
    _description = 'dg.payasos.managers'

    name = fields.Char('Nombre', required=True)
    annos = fields.Integer('Años en la empresa', required=True)

class fiestas(models.Model):
    _name = 'dg.payasos.fiestas'
    _description = 'dg.payasos.fiestas'

    description = fields.Text('Tipo de fiesta', help='Cumpleaños, fin de curso...', required=True)
    fecha = fields.Date('Fecha', required=True)
    direccion = fields.Char('Dirección', required=True)
    hora_comienzo = fields.Float('Hora de comienzo')
    hora_fin = fields.Float('Hora de fin')

class clientes(models.Model):
    _name = 'dg.payasos.clientes'
    _description = 'dg.payasos.clientes'
    _sql_constraints = [
                     ('dni_unique', 
                      'unique(dni)',
                      'ERROR: Ese DNI ya existe')
    ]

    dni = fields.Char('DNI', required=True)
    name = fields.Char('Nombre', required=True)
    edad = fields.Integer('Edad')
    
#
#  @api.depends('value')
#   def _value_pc(self):
#        for record in self:
#            record.value2 = float(record.value) / 100
