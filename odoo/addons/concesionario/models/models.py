# -*- coding: utf-8 -*-

from odoo import models, fields, api

#class EstadoCoches(models.Model):
#    _name='concesionario.coches_kanban'
#    _description = 'concesionario.coches_kanban'
    

class Coches(models.Model):
    _name = 'concesionario.coches'
    _description = 'concesionario.coches'
    marca = fields.Char(string='marca')
    modelo = fields.Char(string='modelo')
    cv = fields.Integer(string="Potencia(CV)")
    color = fields.Char(string="color")
    estado = fields.Selection([
        ('vendido', 'Vendido'),('alquilado','Alquilado'),('reparado','Reparado')
    ], string='estado')
    matricula = fields.Many2one('concesionario.clientes', string="matricula")

    
    

#class CocheCompradoVendido(models.Model):
#    _name ='concesionario.coches_comprado_vendido'
#    _description ='concesionario.coches_comprado_vendido'
    #_inherit = ['concesionario.coches']
    #@api.multi
    #def _selecionarEstado(self):
    #    self.ensure.one()
    #    if self.estado

# class CochesAñadir(models.Model):
#     _name = 'concesionario.coches_annadir'
#     _description = 'concesionario.coches_annadir'
#     marca = fields.Char(string='Marca')
#     modelo = fields.Char(string='Modelo')
#     cv = fields.Integer(string="Potencia(CV)")
#     color = fields.Char('Cplor')
#     estado = fields.Selection([
#         ('vendido', 'Vendido'),('alquilado','Alquilado'),('reparado','Reparado')
#     ], string='estado')
#     matricula = fields.Char(string="matricula")




class Clientes(models.Model):
    _name = 'concesionario.clientes'
    _description = 'concesionario.clientes'
    nombre = fields.Char(string="Nombre" ,required=True)
    apellidos = fields.Char(string="Apellidos" ,required=True)
    direccion = fields.Char(string="Dirección")
    telefono = fields.Integer(string="Teléfono")
    matricula = fields.Char(string="matricula")
    
    
class Empleados(models.Model):
    _name = 'concesionario.empleados'
    _description = 'concesionario.empleados'
    nombre = fields.Char(string='Nombre',required=True )
    apellidos = fields.Char(string="Apellidos")
    nrovendidos = fields.Integer(String="Número de coches vendidos")
    salario = fields.Integer(string="Salario")
    
    

class Mecanicos(models.Model):
    _name = 'concesionario.mecanicos'
    _description = 'concesionario.mecanicos'
    id_mecanico = fields
    nombre = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    salario = fields.Integer(string="Salario")
    numero_reparaciones = fields.Integer(string="Numero de repaciones")



    
    