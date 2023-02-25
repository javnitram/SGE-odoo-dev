# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class concesionario(models.Model):
#     _name = 'concesionario.concesionario'
#     _description = 'concesionario.concesionario'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Coches(models.Model):
    _name = 'concesionario.coches'
    _description = 'concesionario.coches'
    #matricula = fields.Char(string='matricula', required=True)
    marca = fields.Char(string='marca')
    modelo = fields.Char(string='modelo')
    cv = fields.Integer(string="Potencia(CV)")
    color = fields.Char('color')
    estado = fields.Char('estado')
    matricula = fields.Many2one('concesionario.clientes', string='Matricula')

class CochesAñadir(models.Model):
    _name = 'concesionario.coches_annadir'
    _description = 'concesionario.coches_annadir'
    matricula = fields.Char(string='Matricula')
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    cv = fields.Integer(string="Potencia(CV)")
    color = fields.Char('Cplor')
    estado = fields.Char('Estado')
    

class Clientes(models.Model):
    _name = 'concesionario.clientes'
    _description = 'concesionario.clientes'
    nombre = fields.Char(string="Nombre" ,required=True)
    apellidos = fields.Char(string="Apellidos" ,required=True)
    direccion = fields.Char(string="Dirección")
    telefono = fields.Integer(string="Teléfono")
    matricula = fields.Char(string="Coche")
    #matricula_ids = fields.One2many('concesionario.clientes', 'matricula', string='ID Matricula')
    #field_name_ids = fields.One2many('comodel_name', 'inverse_field_name', string='field_name')
    
    
#class Tipo(models.Model):
#    _name = 'concesionario.tipo'
#    _description = 'concesionario.tipo'
#    idCoche = fields.Char('Matricula del coche' ,required=True)
#    estado = fields.Char('Estado',required=True)
#    fechaIn =  fields.Date('Fecha Inicial')
#    fechaFin = fields.Date('Fecha Finalizacion') 
    
class Empleados(models.Model):
    _name = 'concesionario.empleados'
    _description = 'concesionario.empleados'
    nombre = fields.Char(string='Nombre',required=True )
    apellidos = fields.Char(string="Apellidos")
    nrovendidos = fields.Integer(String="Número de coches vendidos")
    salario = fields.Integer(string="Salario")
    #<!--clientevendido = fields.Char('clientevendido')-->

class Mecanicos(models.Model):
    _name = 'concesionario.mecanicos'
    _description = 'concesionario.mecanicos'
    nombre = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)


    
    