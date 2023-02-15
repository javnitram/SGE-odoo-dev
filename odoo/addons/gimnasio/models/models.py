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
    name = fields.Char('Nombre',required=True)
    activo = fields.Boolean('Activo?',default=True)
    telefono = fields.Integer('Telefono',required=True)
    clases_ids = fields.Many2many('ar.gimnasio.clases', string='Clases')
    inscripciones_id = fields.Many2one('ar.gimnasio.inscripciones', string='Inscripcion')

class ClasesGimnasio(models.Model):
    _name = 'ar.gimnasio.clases'
    _description = 'ar.gimnasio.clases'
    
    name = fields.Char('Nombre_clase',required=True)
    precio = fields.Float('Precio',required=True)
    monitor = fields.Char('Monitor',required=True)

    clientes_ids = fields.Many2many('ar.gimnasio.clientes', string='Clientes')
    
class InscripcionesGimnasio(models.Model):
    _name = 'ar.gimnasio.inscripciones'
    _description = 'ar.gimnasio.inscripciones'

    name = fields.Selection([
        ('1 mes', '1 mes'),
        ('3 meses', '3 meses'),
        ('6 meses', '6 meses'),
        ('12 meses', '12 meses')
    ],string='tipo_inscripcion')
    fecha_inscripcion = fields.Date('Fecha de inscripcion',required=True)
    precio = fields.Float('Precio')
    clientesInscripcion_ids = fields.One2many('ar.gimnasio.clientes', 'inscripciones_id', string='Clientes_Inscripcion')

class ProductosGimnasio(models.Model):
    _name = 'ar.gimnasio.productos'
    _description = 'ar.gimnasio.productos'

    name = fields.Char('Nombre del producto',required=True)
    precio = fields.Float('Precio',required=True)
    imagen = fields.Image('Imagen',store=True,relation="res.partner")
    disponibilidad = fields.Boolean('Disponibilidad',default=True)
    descripcion = fields.Char('Descripcion')