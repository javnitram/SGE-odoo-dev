# -*- coding: utf-8 -*-
from xml.dom import ValidationErr
from odoo import models, fields, api

class Coches(models.Model):
    _name = 'concesionario.coches'
    _description = 'concesionario.coches'
    marca = fields.Char(string='marca')
    modelo = fields.Char(string='modelo')
    cv = fields.Integer(string="Potencia(CV)")
    color = fields.Char(string="color")
    estado = fields.Selection([('noasignado','Sin asignar'),('alquilable','Disponible a alquiler'),('enventa','En venta'),
        ('vendido', 'Vendido'),('alquilado','Alquilado'),('reparado','Reparado')
    ], string='estado')
    empleados_ids = fields.One2many('concesionario.empleados', 'empleados_id', string='Empleado encargado')
    matricula = fields.Char(string="matricula")
    imagen = fields.Image('Inserte la imagen del coche', max_width=120, max_height=120)
    
    
    @api.constrains('matricula')
    def verificar_matricula(self):
        for rec in self:
            matricualExiste = self.env['concesionario.coches'].search([('matricula', '=', rec.matricula), ('id','!=',rec.id)])
            if matricualExiste:
                raise ValidationErr(("Matricula %s ya existe" % rec.matricula))


class Clientes(models.Model):
    _name = 'concesionario.clientes'
    _description = 'concesionario.clientes'
    nombre = fields.Char(string="Nombre" ,required=True)
    apellidos = fields.Char(string="Apellidos" ,required=True)
    direccion = fields.Char(string="Dirección")
    telefono = fields.Integer(string="Teléfono")
    matricula = fields.Many2one('concesionario.coches', string="Matricula de coche")

    

class Empleados(models.Model):
    _name = 'concesionario.empleados'
    _description = 'concesionario.empleados'
    id_empleado = fields.Integer(string="Id del empleado",required=True)
    nombre = fields.Char(string='Nombre',required=True )
    apellidos = fields.Char(string="Apellidos")
    nrovendidos = fields.Integer(string="Número de coches vendidos")
    salario = fields.Integer(compute='salario', string='Salario')
    empleados_id = fields.Many2one('concesionario.coches', string='Encargado del coche')

    @api.constrains(id_empleado)
    def verificar_id_empleado(self):
        for rec in self:
            empleadoExiste = self.env['concesionario.empleados'].search([('id_empleado',"=",rec.id_empleado),(('id','!=',rec.id))])
            if empleadoExiste:
                raise ValidationErr(("El empleado %s ya existe!"% rec.id_empleado))
        
    @api.depends('nrovendidos')
    def _compute_field_name(self):
        if self.salario != 0:
            self.salario += self.salario+(1.1*self.nrovendidos)
    

class Mecanicos(models.Model):
    _name = 'concesionario.mecanicos'
    _description = 'concesionario.mecanicos'
    id_mecanico = fields.Integer(string="Id del mecánico",required=True)
    nombre = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    numero_reparaciones = fields.Integer(string="Numero de repaciones")
    salario = fields.Integer(compute='salario', string='Salario') 
    #field_name_ids = fields.Many2many('concesionario.coches_a_repar', string='Field Name')

    @api.constrains(id_mecanico)
    def verificar_id_empleado(self):
        for rec in self:
            empleadoExiste = self.env['concesionario.empleados'].search([('id_mecanico',"=",rec.id_mecanico),(('id','!=',rec.id))])
            if empleadoExiste:
                raise ValidationErr(("El empleado %s ya existe!"% rec.id_mecanico))
   

    @api.depends('numero_reparaciones')
    def _compute_field_name(self):
        if self.salario != 0:
            self.salario += self.salario+(1.15*self.numero_reparaciones)
   


class Coches_A_Reparar(models.Model):
    _name = 'concesionario.coches_a_reparar'
    _description = 'concesionario.coches_a_reparar'
    id_mecanico = fields.Integer('Id del mecánico')
    nombre_mecanico = fields.Char('Nombre mecánico')
    matricula_coche = fields.Integer('Matricula del coche')
    modelo_coche = fields.Char('Modelo del coche')
    fecha_incial_reparacion = fields.Datetime('fecha_incial_reparacion')
    fecha_final_reparacion = fields.Datetime('fecha_final_reparacion')
    coste_reparacion = fields.Integer(string='coste_reparacion')
    
    @api.onchange('coste_reparacion')
    def _onchange_(self):
        self.coste_reparacion = self.coste_reparacion