# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class armas(models.Model):
#     _name = 'armas.armas'
#     _description = 'armas.armas'

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


class Armas(models.Model):
    _name = 'ac.armas.categoria'
    _description = 'Armas'
    
    nombre_arma = fields.Char('nombre_arma')
    precio = fields.Float('precio')
    referencia = fields.Char('referencia')
    categoria = fields.Selection([
        ('1', 'Fusil de asalto'),('2', 'Subfusil'),('3','Escopeta'),('4','Francotirador'),('5','Lanzacohetes')
    ], string='categoria')
    disponibilidad = fields.Boolean('disponobilidad')


class accesoriosArmas(models.Model):
    _name = 'ac.accesorios.armas'
    _description = 'AccesoriosArmas'

    nombre_accesorio = fields.Char('nombre_accesorio')
    precio = fields.Float('precio')
    referencia = fields.Char('referencia')
    disponibilidad = fields.Boolean('disponobilidad')


class camuflajesArmas(models.Model):
    _name = 'ac.camuflajes.armas'
    _description = 'CamuflajesArmas'

    nombre_camuflaje = fields.Char('nombre_camuflaje')
    precio = fields.Float('precio')
    referencia = fields.Char('referencia')
    disponibilidad = fields.Boolean('disponobilidad')


class clientes(models.Model):
    _name = 'ac.clientes.tienda'
    _description = 'Clientes'

    nombre_cliente = fields.Char('nombre_cliente')
    telefono = fields.Integer('telefono')
    fecha_nacimiento = fields.Date('fecha_nacimiento')
    direccion = fields.Char('direccion')
        
        
        