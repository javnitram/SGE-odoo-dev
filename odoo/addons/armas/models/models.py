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
    
    name = fields.Char('Nombre del arma:')
    precio = fields.Float('Precio:')
    referencia = fields.Char('Referencia:')
    categoria = fields.Selection([
        ('1', 'Fusil de asalto'),('2', 'Subfusil'),('3','Escopeta'),('4','Francotirador'),('5','Lanzacohetes')
    ], string='categoria')
    disponibilidad = fields.Boolean('Disponibilidad:')
    imagen = fields.Image('Imagen del arma', store=True, relation="res.partner")
    camuflaje_id = fields.Many2one('ac.camuflajes.armas', string='Camuflaje')
    accesorios_id = fields.Many2one('ac.accesorios.armas', string='Accesorios')
    clientes_ids = fields.Many2many('ac.clientes.tienda', string='Cliente')
    
    
    


class accesoriosArmas(models.Model):
    _name = 'ac.accesorios.armas'
    _description = 'AccesoriosArmas'

    name = fields.Char('Nombre del accesorio:')
    precio = fields.Float('Precio:')
    referencia = fields.Char('Referencia:')
    disponibilidad = fields.Boolean('Disponibilidad:')
    accesorios_ids = fields.One2many('ac.armas.categoria', 'accesorios_id', string='Accesorios')
    
    


class camuflajesArmas(models.Model):
    _name = 'ac.camuflajes.armas'
    _description = 'CamuflajesArmas'

    name = fields.Char('Nombre del camuflaje:')
    precio = fields.Float('Precio:')
    referencia = fields.Char('Referencia:')
    disponibilidad = fields.Boolean('Disponibilidad:')
    camuflajes_ids = fields.One2many('ac.armas.categoria', 'camuflaje_id', string='Camuflajes')
    


class clientes(models.Model):
    _name = 'ac.clientes.tienda'
    _description = 'Clientes'

    name = fields.Char('Nombre del cliente:')
    telefono = fields.Integer('Teléfono:')
    fecha_nacimiento = fields.Date('Fecha de nacimiento:')
    direccion = fields.Char('Dirección:')
    arma_ids = fields.Many2many('ac.armas.categoria', string='Arma')
        
        
        