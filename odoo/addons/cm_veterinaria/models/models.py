# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VeterinariaMascotas(models.Model):
    _name = 'cm.veterinaria.mascotas'
    _description = 'veterinaria.mascotas'
    name = fields.Char('Name',required=True)
    fotoPet = fields.Image(string='Photo', max_width=265, max_height=300,store=True,relation="res.partner",help="Select picture here")    
    petNum = fields.Char('Pet Number',required=True)    
    race = fields.Selection([
        ('0', 'Dog'),
        ('1', 'Cat')
    ], string='Race',required=True)
    owner_id = fields.Many2one('cm.veterinaria.cliente', string='Owner')
    veterinarianName_id = fields.Many2one('cm.veterinaria.veterinario', string='Veterinarian Name')
    healthInsurance = fields.Boolean('Health Insurance',required=True)
    registrationDate = fields.Date('Registration Date',required=True)
    vaccinesDone_ids = fields.Many2many('cm.veterinaria.vacunas', string='Vaccines Done')
        

class VeterinariaVacunas(models.Model):
    _name = 'cm.veterinaria.vacunas'
    _description = 'veterinaria.vacunas'
    name = fields.Char('Vaccine',required=True,delegate=['vaccine_ids'])
    animalTree = fields.Selection([
        ('0', 'Dog'),
        ('1', 'Cat')
    ], string='Race',required=True)
    weekToVaccinate = fields.Integer('Weeks',required=True)
    vaccine_ids = fields.Many2many('cm.veterinaria.mascotas', string='Vaccines')
   
class VeterinariaVeterinario(models.Model):
    _name = 'cm.veterinaria.veterinario'
    _description = 'veterinaria.veterinario'
    name = fields.Char('Name',required=True)
    empnum = fields.Char('Employee Number',required=True)
    room_id = fields.Many2one('cm.veterinaria.salas', string='Room')
    category = fields.Selection([
       ('0', 'Veterinary Assistant'),
       ('1', 'Veterinarian'),
       ('2', 'Veterinary Surgeon'),
       ('3', 'Boss/Owner')
    ], string='Category',required=True)
    

class VeterinariaCliente(models.Model):
    _name = 'cm.veterinaria.cliente'
    _description = 'veterinaria.cliente'
    name = fields.Char('Nombre',required=True)
    clientNum = fields.Char('Client Number',required=True)    
    clientRegistrationDate = fields.Date('Client Registration Date',required=True)
    mascotas_ids = fields.One2many('cm.veterinaria.mascotas', 'owner_id', string='Mascotas')
    numberOfPets = fields.Integer('Number Of Pets', compute='conteoMascotas', store=True, readonly=True)

    @api.depends('mascotas_ids')
    def conteoMascotas(self):
        for r in self:
            r.numberOfPets = len(r.mascotas_ids)

class VeterinariaSalas(models.Model):
    _name = 'cm.veterinaria.salas'
    _description = 'veterinaria.salas'
    name = fields.Char('Room',required=True)
    veterinarian_ids = fields.One2many('cm.veterinaria.veterinario', 'room_id', string='Employee')

    #vaccinated = fields.Selection([
   #    ('0', 'Yes'),
    #   ('1', 'Pending')
   # ], string='Vaccinated',required=True)
   # vaccineDate = fields.Date('Vaccine Date')

# class cm_veterinaria(models.Model):
#     _name = 'cm_veterinaria.cm_veterinaria'
#     _description = 'cm_veterinaria.cm_veterinaria'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
