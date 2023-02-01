# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TabernaCategoria(models.Model):
    _name = 'jm.taberna.categoria'
    _description = 'jm.taberna.categoria'
    nombre = fields.Char('nombre', required=True)


class TabernaBebidas(models.Model):
    _name = 'jm.taberna.bebidas'
    _description = 'jm.taberna.bebidas'
    id_bebida = fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    alcohol = fields.Boolean('alcohol', required=True)
    tipo = fields.Char('tipo', required=True)
    pais = fields.Char('pais', required=True)

class TabernaComidas(models.Model):
    _name = 'jm.taberna.comidas'
    _description = 'jm.taberna.comidas'
    id_comida = fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    vegetariano = fields.Boolean('vegetariano', required=True)

class TabernaEmpleados(models.Model):
    _name = 'jm.taberna.empleados'
    _description = 'jm.taberna.empleados'
    id_empleado = fields.Integer('id', required=True)
    nombre = fields.Char('nombre', required=True)
    apellido1 = fields.Char('apellido1', required=True)
    apellido2 = fields.Char('apellido2')
    edad = fields.Integer('edad')
    salario = fields.Float('salario')
    telefono = fields.Integer('telefono', required=True)
    

# classpaisuired
# salario = fields.Float('salario')=Truern, re, requ, required=Trueired=Trueq
# tipo = fields.Char('tipo', required=True)uired=Truea(models., required=TrueModel):
#     _name = 'taberna.taberna'
#     _description = 'taberna.taberna'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
