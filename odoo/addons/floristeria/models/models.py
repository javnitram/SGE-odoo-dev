# -*- coding: utf-8 -*-

from odoo import models, fields, api

class manager(models.Model):
    _name = 'hf_floristeria_manager'
    _description = 'Encargados'
    name = fields.Char('Nombre')
    bouquet_ids = fields.One2many('hf_floristeria_bouquet', 'manager_id', string=' Ramos de flores')
    flower_pot_ids = fields.One2many('hf_floristeria_flower_pot', 'manager_id', string=' Macetas')

class flower(models.Model):
    _name = 'hf_floristeria_flower'
    _description = 'Flores'
    name = fields.Char(string='Nombre común',required=True, help='')
    bouquet_ids = fields.Many2many('hf_floristeria_bouquet', string=' Ramos de flores')
    flower_pot_ids = fields.Many2many('hf_floristeria_flower_pot', string=' Macetas')
    specie_id = fields.Many2one('hf_floristeria_specie', string='Especie', required=True)

    scientific_name = fields.Char(string='Nombre científico', required=True, help='')
    main_color = fields.Char(string='Color predominante', help='')
    subgroup_gim = fields.Selection([
        ('0', ''),
        ('1', 'Cícadas'),
        ('2', 'Ginko'),
        ('3', 'Coníferas'),
        ('4', 'Gnetales')
    ], string='Subgrupo de las gimnospermas')
    subgroup_ang = fields.Selection([
        ('0', ''),
        ('1', 'Amborellales'),
        ('2', 'Nymphaeales'),
        ('3', 'Austrobaileyales'),
        ('4', 'Chloranthales'),
        ('5', 'Magnólidas'),
        ('6', 'Ceratophyllales'),
        ('7', 'Eudicotiledóneas'),
        ('8', 'Monocotiledóneas')
    ], string='Subgrupo de las angiospermas')
    flower_image = fields.Image('Imagen')
    
class specie(models.Model):
    _name = 'hf_floristeria_specie'
    _description = 'Especies'
    name = fields.Selection([
        ('Gimnospermas', 'Gimnospermas'),
        ('Angiospermas', 'Angiospermas')
    ], string='Especie', required=True)
    flower_ids = fields.One2many('hf_floristeria_flower', 'specie_id', string=' Flores')
    
class bouquet(models.Model):
    _name = 'hf_floristeria_bouquet'
    _description = 'Ramo de flores'
    name = fields.Char('Nombre', required=True)
    flower_ids = fields.Many2many('hf_floristeria_flower', string=' Flores')
    manager_id = fields.Many2one('hf_floristeria_manager', string=' Encargado')
    
    size = fields.Selection([
        ('s', 'Pequeño'),
        ('m', 'Normal'),
        ('l', 'Grande')
    ], string='Tamaño',required=True)
    bouquet_image = fields.Image('Imagen')

    price = fields.Float(compute='_compute_price', string='Precio')
    
    @api.depends('price', 'size', 'flower_ids')
    def _compute_price(self):
        for rec in self:
            if(rec.size == 's'):
                base_price = 15
            elif(rec.size == 'm'):
                base_price = 25
            elif(rec.size == 'l'):
                base_price = 40
            else:
                base_price = 10
            rec.price = base_price + (len(rec.flower_ids) * 1.5)

class flower_pot(models.Model):
    _name = 'hf_floristeria_flower_pot'
    _description = 'Macetas'
    name = fields.Char('Nombre', required=True)
    flower_ids = fields.Many2many('hf_floristeria_flower', string=' Flores')
    manager_id = fields.Many2one('hf_floristeria_manager', string=' Encargado')
    
    size = fields.Selection([
        ('0', ''),
        ('1', 'Pequeño'),
        ('2', 'Normal'),
        ('3', 'Grande')
    ], string='Tamaño',required=True)
