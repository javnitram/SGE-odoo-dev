# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalDoctores(models.Model):
    _name="hospital.doctores"
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    specialty=fields.Char(string = "Especialidad",required=True,help="Introduce la especialidad")

class HospitalPacientes(models.Model):
    _name="hospital.pacientes"
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string="Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    history=fields.Char(string="Historia",required=True,help="Introduce la razón de visita al hospital")
    alergias=fields.Char(string="Alergias",help="Posible alergia a medicamentos")

class HospitalEnfermeros(models.Model):
    _name="hospital.enfermeros"
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string = "Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    specialty=fields.Char(string = "Especialidad",required=True,help="Introduce la especialidad")

class HospitalTratamientos(models.Model):
    _name="hospital.tratamientos"
    name=fields.Char(string="Nombre",required=True,help="Introduce el nombre")
    surname=fields.Char(string="Apellido",required=True,help="Introduce el apellido")
    date=fields.Date(string="Fecha de nacimiento")
    history=fields.Char(string="Historia",required=True,help="Introduce la razón de visita al hospital")
    alergias=fields.Char(string="Alergias",help="Posible alergia a medicamentos")


