# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalDoctores(models.Model):
    _name="gs.hospital.doctores"
    _description = 'gs.hospital.doctores'
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(string="Teléfono")
    especialidad=fields.Selection([('0','Infectología y nefrología'),('1','Inmunología'),('2','Oncología'),
    ('3','General')],string = "Especialidad",help="Introduce la especialidad")
    imagen = fields.Image(string="Imagen",store=True)
    pacientes_ids = fields.One2many('gs.hospital.pacientes', 'doctor_id', string='Pacientes')
    
class HospitalPacientes(models.Model):
    _name="gs.hospital.pacientes"
    _description = 'gs.hospital.pacientes'
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string="Apellido",required=True,help="Introduce el apellido")
    sexo=fields.Selection([('0','Masculino'),('1','Femenino')],string="Sexo",required=True)
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(string="Teléfono")
    history=fields.Char(string="Historia",required=True,help="Introduce la razón de visita al hospital")
    alergias=fields.Char(string="Alergias",help="Posible alergia a medicamentos")
    doctor_id = fields.Many2one('gs.hospital.doctores', string='Doctor')
    enfermero_ids = fields.Many2many('gs.hospital.enfermeros', string='Enfermero')
    medicinas_ids = fields.Many2many('gs.hospital.medicinas', string='Medicinas')

class HospitalEnfermeros(models.Model):
    _name="gs.hospital.enfermeros"
    _description = 'gs.hospital.enfermeros'
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")    
    sexo=fields.Selection([('0','Masculino'),('1','Femenino')],string="Sexo",required=True)
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(string="Teléfono")
    pacientes_ids = fields.Many2many('gs.hospital.pacientes',string='Pacientes');

class HospitalMedicinas(models.Model):
    _name="gs.hospital.medicinas"
    _description = 'gs.hospital.medicinas'
    nroserie=fields.Char(string="Número de serie",required=True)
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    cantidad=fields.Integer(string="Cantidad", required=True)
    tipo=fields.Selection([('0','Analgésicos y antipiréticos'),('1','Antibióticos betalactámicos'),
                           ('2','Inhibidores de la angiotensina')],string = "Tipo de medicamento")
    imagen = fields.Image(string="Imagen",store=True)