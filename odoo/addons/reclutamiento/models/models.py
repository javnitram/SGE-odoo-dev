# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ejercito(models.Model):
    _name = 'ac.reclutamiento.ejercito'
    _description = 'ac.reclutamiento.ejercito'
    id_ejercito= fields.Integer()
    nombre = fields.Char()
  


class infanteria_CaC(models.Model):
    _name = 'ac.reclutamiento.infanteria.cac'
    _description = 'ac.reclutamiento.infanteria.cac'
    nombre = fields.Char()
    descripcion = fields.Text()
    armadura = fields.Selection([
        ('1', 'ligera')
        ,('2','media')
        ,('3','pesada')
    ], string='armadura')

class infanteria_proyectiles(models.Model):
    _name = 'ac.reclutamiento.infanteria.proyectiles'
    _description = 'ac.reclutamiento.infanteria.proyectiles'
    nombre = fields.Char()
    descripcion = fields.Text()
    municion= fields.Integer()
    ##poner valor por defecto
    alcance= fields.Integer()

class undiades_motadas(models.Model):
    _name = 'ac.reclutamiento.unidades.montadas'
    _description = 'ac.reclutamiento.montadas'
    nombre = fields.Char()
    descripcion = fields.Text()
    monturas = fields.Selection([
        ('1', 'caballo'),('2','camello'),('3','elefante')
    ], string='montura')
    ##atributo calculado
    ##velocidad= flieds.integer()
    ##
class artilleria(models.Model):
    _name = 'ac.reclutamiento.artilleria'
    _description = 'ac.reclutamiento.artilleria'
    nombre = fields.Char()
    descripcion = fields.Text()
    municion = fields.Selection([
        ('1', 'piedra'),('2','virote')
    ], string='municion')    
    ##poner valor por defecto
    alcance= fields.Integer()
    

   ## @api.depends('value')
    ##def _value_pc(self):
        ##for record in self:
            ##record.value2 = float(record.value) / 100
