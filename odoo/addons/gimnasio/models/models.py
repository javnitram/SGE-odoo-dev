# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gimnasio(models.Model):
#     _name = 'gimnasio.gimnasio'
#     _description = 'gimnasio.gimnasio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


from odoo import models,api,fields


class ClientesGimnasio(models.Model):
    _name = 'ar.gimnasio.clientes'
    _description = 'ar.gimnasio.clientes'

    dni = fields.Char('DNI',required=True)
    nombre = fields.Char('Nombre',required=True)
    activo = fields.Boolean('Activo?',default=True)
    telefono = fields.Integer('telefono',required=True)

class ClasesGimnasio(models.Model):
    _name = 'ar.gimnasio.clases'
    _description = 'ar.gimnasio.clases'
    
    nombre_clase = fields.Char('nombre_clase',required=True)
    precio = fields.Float('precio',required=True)
    monitor = fields.Char('monitor',required=True)
    
class InscripcionesGimnasio(models.Model):
    _name = 'ar.gimnasio.inscripciones'
    _description = 'ar.gimnasio.inscripciones'

    tipo_inscripcion = fields.Selection([
        ('0', '1 mes'),
        ('1', '3 meses'),
        ('2', '6 meses'),
        ('3', '12 meses')
    ],string='tipo_inscripcion')
    fecha_inscripcion = fields.Date('fecha_inscripcion',required=True)
    precio = fields.Float('precio')

class ProductosGimnasio(models.Model):
    _name = 'ar.gimnasio.productos'
    _description = 'ar.gimnasio.productos'

    nombre_producto = fields.Char('nombre_producto',required=True)
    precio = fields.Float('precio',required=True)
    disponibilidad = fields.Boolean('disponibilidad',default=True)
    descripcion = fields.Char('descripcion')