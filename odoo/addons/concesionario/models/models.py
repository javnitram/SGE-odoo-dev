# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConcesionarioMarcas(models.Model):
    _name = 'dhm.concesionario.marcas'
    _description = 'Marcas'
    id = fields.Integer('Id',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre de la marca')

class ConcesionarioModelo(models.Model):
    _name = 'dhm.concesionario.modelo'
    _description = 'Modelos'
    id = fields.Integer('Id',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre del modelo')
    estado = fields.Selection([
        ('0', 'Nuevo'),
        ('1', 'KM-0'),
        ('2', 'Seminuevo'),
        ('3', 'Fallos'),
        ('4', 'Desguaze')
    ], string='Estado')

class ConcesionarioMotorizacion(models.Model):
    _name = 'dhm.concesionario.motorizacion'
    _description = 'Motorizacion'
    id = fields.Integer('Id',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca la motorizacion del modelo')
    caballos = fields.Integer('Caballos',required=True)
    cilindrada = fields.Char('Cilindrada',required=True,help='Introduzca la cilindrada del modelo')


class ConcesionarioCaracteristicas(models.Model):
    _name = 'dhm.concesionario.caracteristicas'
    _description = 'Caracteristicas'
    id = fields.Integer('Id',required=True)
    nombre = fields.Char('Nombre',required=True,help='Introduzca el nombre de la caracteristica')
    descripcion = fields.Char('Descripcion',required=True,help='Introduzca la descricion de la caracteristica')
    