# -*- coding: utf-8 -*-

from odoo import models, fields, api


class payasos(models.Model):
    _name = 'dg.payasos.payasos'
    _description = 'dg.payasos.payasos'
    _sql_constraints = [
                     ('tarifa_check', 
                      'check(tarifa>0 AND tarifa<100)',
                      'ERROR: La tarifa debe estar entre el rango de 0 y 100'),
                      ('edad_check', 
                      'check(edad>16)',
                      'ERROR: El payaso debe tener edad legal para trabajar')
    ]
    
    name = fields.Char('Nombre', required=True)
    description = fields.Text('Descripcion', help='Breve descripcion del payaso')
    edad = fields.Integer('Edad', required=True)
    color_nariz = fields.Selection([
        ('r', 'rojo'),
        ('v', 'verde'),
        ('ac', 'azul celeste'),
        ('m', 'morado'),
        ('a', 'amarillo'),
        ('n', 'naranja'),
    ], string='Color de nariz', required=True, default=0)
    tarifa = fields.Float('tarifa', required=True)
    manager_id = fields.Many2one('dg.payasos.managers', string='Manager')
    fiestas_ids = fields.Many2many('dg.payasos.fiestas', string='Fiestas asistidas')
    

class managers(models.Model):
    _name = 'dg.payasos.managers'
    _description = 'dg.payasos.managers'
    _sql_constraints = [
                     ('annos_check', 
                      'check(NOT annos < 0)',
                      'ERROR: Los años no pueden ser negativos')
    ]
    
    name = fields.Char('Nombre', required=True)
    annos = fields.Integer('Años en la empresa', required=True)
    foto = fields.Image(string="Foto",store=True,relation="res.partner",help="Agregar imagen")
    payasos_ids = fields.One2many('dg.payasos.payasos', 'manager_id', string='Payasos manejados')
    

class fiestas(models.Model):
    _name = 'dg.payasos.fiestas'
    _description = 'dg.payasos.fiestas'
    _sql_constraints = [
                     ('horasDia_check', 
                      'check(hora_comienzo >=6 AND hora_fin < 24)',
                      'ERROR: Nuestra empresa atiende fiestas dentro de nuestro horario: 6:00 AM - 23:59 PM'),
                      ('horaReal_check', 
                      'check(hora_comienzo < hora_fin)',
                      'ERROR: La fiesta no puede acabar antes de que comience'),
                      ('duracionMinima_check', 
                      'check((hora_fin - hora_comienzo) >= 0.5)',
                      'ERROR: La fiesta debe durar un mínimo de 30 minutos')
    ]

    description = fields.Text('Tipo de fiesta', help='Cumpleaños, fin de curso...', required=True)
    fecha = fields.Date('Fecha', required=True)
    direccion = fields.Char('Dirección', required=True)
    hora_comienzo = fields.Float('Hora de comienzo')
    hora_fin = fields.Float('Hora de fin')
    cliente_id = fields.Many2one('dg.payasos.clientes', string='Organizador')
    payasos_ids = fields.Many2many('dg.payasos.payasos', string='Payasos asistentes', required=True)
    

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
    fiestas_ids = fields.One2many('dg.payasos.fiestas', 'cliente_id', string='Fiestas organizadas')