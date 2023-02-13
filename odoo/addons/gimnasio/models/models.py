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
    telefono = fields.Integer('Telefono',required=True)


class ClasesGimnasio(models.Model):
    _name = 'ar.gimnasio.clases'
    _description = 'ar.gimnasio.clases'
    
    nombre_clase = fields.Char('Nombre_clase',required=True)
    precio = fields.Float('Precio',required=True)
    monitor = fields.Char('Monitor',required=True)
    
class InscripcionesGimnasio(models.Model):
    _name = 'ar.gimnasio.inscripciones'
    _description = 'ar.gimnasio.inscripciones'

    tipo_inscripcion = fields.Selection([
        ('0', '1 mes'),
        ('1', '3 meses'),
        ('2', '6 meses'),
        ('3', '12 meses')
    ],string='tipo_inscripcion')
    fecha_inscripcion = fields.Date('Fecha de inscripcion',required=True)
    precio = fields.Float('Precio')

class ProductosGimnasio(models.Model):
    _name = 'ar.gimnasio.productos'
    _description = 'ar.gimnasio.productos'

    nombre_producto = fields.Char('Nombre del producto',required=True)
    precio = fields.Float('Precio',required=True)
    disponibilidad = fields.Boolean('Disponibilidad',default=True)
    descripcion = fields.Char('Descripcion')