# -*- coding: utf-8 -*-
from odoo import models, fields, api

class empleado(models.Model):
    _name = 'cinema.empleado'
    dni = fields.Char(string="DNI", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Integer(string="Número de teléfono")
    puesto = fields.Char(string="Puesto de trabajo")

class cliente(models.Model):
    _name = 'cinema.cliente'
    name = fields.Integer(string  = "Nº Cliente", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    telefono = fields.Integer(string = "Número de teléfono")
    cod_postal = fields.Integer(string = "Código postal")
       
class peliculas(models.Model):
    _name = 'cinema.pelicula'
    name = fields.Char(string  = "ID_pelicula", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    sinopsis = fields.Char(string="Sinopsis", required = True)
    duracion = fields.Integer(string = "Duracion")
    fecha_estreno = fields.Date(string = "Fecha de estreno")
    distribuidora = fields.Many2One("cinema.distribuidora",string = "Distribuidora")

class distribuidora(models.Model):
    _name = "cinema.distribuidora"
    name = fields.Integer(string = "ID_distribuidora", required=True)
    nombre = fields.Char(string = "Nombre Distribuidora", required=True)
    pelicula = fields.One2Many("cinema.pelicula","distribuidora",string="Pelicula")

class sesion(models.Model):
    _name = "cinema.sesion"
    numero_sala = fields.Integer(string = "Nº de sala")
    pelicula = fields.Many2one("cinema.pelicula",string = "Pelicula")
    fecha_sesion = fields.Date(string = "Fecha de la sesion, incluye hora")