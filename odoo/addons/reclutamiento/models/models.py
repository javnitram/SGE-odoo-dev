# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ejercito(models.Model):
    _name = 'ac.reclutamiento.ejercito'
    _description = 'ac.reclutamiento.ejercito'
    nombre = fields.Char()
    unidades= fields.Integer()
    general = fields.Many2one('ac.reclutamiento.general', string='nombre')

class general(models.Model):
    _name = 'ac.reclutamiento.general'
    _description = 'ac.reclutamiento.general'
    imagen= fields.Image(string="imagen",store=True,relation="res.partner",help="Inserte la imagen aqui")
    nombre = fields.Char()
    edad= fields.Char() 
    ejercitos_gestionados = fields.One2many('ac.reclutamiento.ejercito', 'nombre', string='ejercitos_gesionados')
  
  


class infanteria_CaC(models.Model):
    _name = 'ac.reclutamiento.infanteria.cac'
    _description = 'ac.reclutamiento.infanteria.cac'
    nombre = fields.Char()
    descripcion = fields.Text()
    armadura = fields.Selection([
        ('1', 'Ligera')
        ,('2','Media')
        ,('3','Pesada')
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
        ('1', 'Caballo'),
        ('2','Camello'),
        ('3','Elefante')
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
        ('1', 'piedra'),
        ('2','virote')
    ], string='municion')    
    ##poner valor por defecto
    alcance= fields.Integer()
    

class campana(models.Model):
    _name = 'ac.reclutamiento.campana'
    _description = 'ac.reclutamiento.campana'
    nombre = fields.Char()
    pais_id = fields.Many2one('res.country', string='Pais')
    fecha_inicio= fields.Date()
    ##poner valor por defecto
    

   ## @api.depends('value')
    ##def _value_pc(self):
        ##for record in self:
            ##record.value2 = float(record.value) / 100
