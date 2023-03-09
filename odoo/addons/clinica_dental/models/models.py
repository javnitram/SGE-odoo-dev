# -*- coding: utf-8 -*-

from odoo import models, fields, api


class clinica_dental(models.Model):
    _name = 'ab.clinica_dental.clinica_dental'
    _description = 'ab.clinica_dental.clinica_dental'
    name = fields.Char(String = "nombre", required=True ,help="introduce el nombre")
 

class Paciente(models.Model):
    _name = 'ab.clinica_dental.paciente'
    _description = 'Información del paciente'
    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')
    telefono = fields.Char(string='Teléfono')
    correo_electronico = fields.Char(string='Correo electrónico')
    historial_clinico = fields.Text(string='Historial clínico')


class CitaDental(models.Model):
     _name = 'ab.clinica_dental.cita_dental'
     _description = 'Información de la cita dental'
     paciente_id = fields.Many2one(comodel_name='ab.clinica_dental.paciente', string='Paciente')
     profesional_dental_id = fields.Many2one(comodel_name='ab.clinica_dental.profesional_dental', string='Profesional dental')
     fecha_hora = fields.Datetime(string='Fecha y hora')
     procedimiento = fields.Text(string='Procedimiento')
     precio = fields.Float(string='Precio')
     estado = fields.Selection(string='Estado', selection=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada')])
   

class ProfesionalDental(models.Model):
     _name = 'ab.clinica_dental.profesional_dental'
     _description = 'Información del profesional dental'
     name = fields.Char(string='Nombre', required=True)
     apellido = fields.Char(string='Apellido', required=True)
     fecha_ingreso = fields.Date(string='Fecha de ingreso')
     especialidad = fields.Selection(string='Especialidad', selection=[('cirugia', 'Cirugía'), ('ortodoncia', 'Ortodoncia'), ('endodoncia', 'Endodoncia')])
     telefono = fields.Char(string='Teléfono')
     correo_electronico = fields.Char(string='Correo electrónico')
     image = fields.Binary(string='Imagen',store=True,relation="res.partner") 

class Tratamiento(models.Model):
    _name = 'ab.clinica_dental.tratamiento'
    _description = 'Información del tratamiento'
    paciente_id = fields.Many2one(comodel_name='ab.clinica_dental.paciente', string='Paciente')
    profesional_dental_id = fields.Many2one(comodel_name='ab.clinica_dental.profesional_dental', string='Profesional dental')
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de fin')
    descripcion = fields.Text(string='Descripción')
    costo_total = fields.Float(string='Costo total', compute='_compute_costo_total')
    linea_ids = fields.One2many(comodel_name='ab.clinica_dental.tratamiento.linea', inverse_name='tratamiento_id', string='Líneas del tratamiento')

    @api.depends('linea_ids')
    def _compute_costo_total(self):
        for tratamiento in self:
            costo_total = sum(tratamiento.linea_ids.mapped('precio'))
            tratamiento.costo_total = costo_total

class TratamientoLinea(models.Model):
    _name = 'ab.clinica_dental.tratamiento.linea'
    _description = 'Línea del tratamiento'
    tratamiento_id = fields.Many2one(comodel_name='ab.clinica_dental.tratamiento', string='Tratamiento')
    procedimiento = fields.Text(string='Procedimiento')
    precio = fields.Float(string='Precio')

class SeguroMedico(models.Model):
    _name = 'ab.clinica_dental.seguro_medico'
    _description = 'Información del seguro médico'
    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    pacientes_ids = fields.Many2many(comodel_name='ab.clinica_dental.paciente', string='Pacientes')