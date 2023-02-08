# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ejercito(models.Model):
    _name = 'ac.reclutamiento.ejercito'
    _description = 'ac.reclutamiento.ejercito'
    id_ejercito= fields.Integer(required=True)
    nombre = fields.Char()
    unidades= fields.Integer()

class general(models.Model):
    _name = 'ac.reclutamiento.general'
    _description = 'ac.reclutamiento.general'
    id_general= fields.Integer(required=True)
    nombre = fields.Char()
    edad= fields.Char() 
  
  


class infanteria_CaC(models.Model):
    _name = 'ac.reclutamiento.infanteria.cac'
    _description = 'ac.reclutamiento.infanteria.cac'
    id_cac= fields.Integer(required=True) 
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
    id_proyectiles=fields.Integer(required=True) 
    nombre = fields.Char()
    descripcion = fields.Text()
    municion= fields.Integer()
    ##poner valor por defecto
    alcance= fields.Integer()


class undiades_motadas(models.Model):
    _name = 'ac.reclutamiento.unidades.montadas'
    _description = 'ac.reclutamiento.montadas'
    id_montadas= fields.Integer(required=True) 
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
    id_artilleria= fields.Integer(required=True) 
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
