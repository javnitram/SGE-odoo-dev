# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalDoctores(models.Model):
    _name="gs.hospital.doctores"
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(string="Teléfono")
    especialidad=fields.Selection([('0','Cirugía'),('1','General'),('2','Traumatología'),('3','Oftalmología')],string = "Especialidad",help="Introduce la especialidad")

class HospitalPacientes(models.Model):
    _name="gs.hospital.pacientes"
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string="Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(int="Teléfono")
    history=fields.Char(string="Historia",required=True,help="Introduce la razón de visita al hospital")
    alergias=fields.Char(string="Alergias",help="Posible alergia a medicamentos")

class HospitalEnfermeros(models.Model):
    _name="gs.hospital.enfermeros"
    dni=fields.Char(string="DNI",required=True)
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")
    sexo=fields.Boolean(bool="Sexo",required=True)
    date=fields.Date(string="Fecha de nacimiento")
    tlf=fields.Integer(int="Teléfono")

class HospitalMedicinas(models.Model):
    _name="gs.hospital.medicinas"
    nroserie=fields.Char(string="Número de serie",required=True)
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    cantidad=fields.Integer(int="Cantidad", required=True)
    tipo=fields.Char(string="Tipo de medicamento")

