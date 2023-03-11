# -*- coding: utf-8 -*-
from odoo import models, fields, api

class empleado(models.Model):
    _name = 'jd_cinema.empleado'
    dni = fields.Char(string="DNI", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    telefono = fields.Integer(string="Número de teléfono")
    puesto = fields.Char(string="Puesto de trabajo")

class cliente(models.Model):
    _name = 'jd_cinema.cliente'
    name = fields.Integer(string  = "Nº Cliente", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    telefono = fields.Integer(string = "Número de teléfono")
    cod_postal = fields.Integer(string = "Código postal")
    empleado_ids = fields.Many2many("jd_cinema.empleado",string="Encargado de ventas")
   
    
       
class peliculas(models.Model):
    _name = 'jd_cinema.pelicula'
    name = fields.Char(string  = "ID_pelicula", required = True)
    nombre = fields.Char(string = "Nombre", required = True)
    sinopsis = fields.Char(string="Sinopsis", required = True)
    duracion = fields.Integer(string = "Duracion")
    fecha_estreno = fields.Date(string = "Fecha de estreno")
    distribuidora = fields.Many2one("jd_cinema.distribuidora",string = "Distribuidora")
    cartelera = fields.Image(string = "Cartelera")

class distribuidora(models.Model):
    _name = "jd_cinema.distribuidora"
    name = fields.Char(string = "ID_distribuidora", required=True)
    nombre = fields.Char(string = "Nombre Distribuidora", required=True)
    pelicula = fields.One2many("jd_cinema.pelicula","distribuidora",string="Pelicula")

class sesion(models.Model):
    _name = "jd_cinema.sesion"
    numero_sala = fields.Integer(string = "Nº de sala")
    pelicula = fields.Many2one("jd_cinema.pelicula",string = "Pelicula")
    fecha_sesion = fields.Datetime(string = "Fecha de la sesion, incluye hora")