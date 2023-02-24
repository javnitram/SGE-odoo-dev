# -*- coding: utf-8 -*-

from odoo import models, fields

class Users(models.Model):
    _name = "ws.users"
    _description = "Users Model"
    name = fields.Char('name')
    phone = fields.Char('phone')
    email = fields.Char('email')


class Technicians(models.Model):
    _name = "ws.technicians"
    _description = "Technician Model"

    name = fields.Char('name')
    photo = fields.Image('photo', max_width=512, max_height=512)


class Repairments(models.Model):
    _name = 'ws.repairments'
    _description = 'Repair Model'
    repair_status = fields.Selection([
        ('inspection_pending', 'Inspection pending'),
        ('quote', 'Quote'),
        ('rejected', 'Rejected'),
        ('accepted', "Accepted"),
        ('processing', "In process"),
        ('ready', 'Ready to pickup'),
        ('completed', 'Completed')
    ], string='repair_status')
    start_date = fields.Date('start_date')
    completion_date = fields.Date('completion_date')
    labor_cost = fields.Float('labor_cost')


class Replacements(models.Model):
    _name = "ws.replacements"
    _description = "Replacement Model"
    old_part_id = fields.Many2one('comodel_name', string='old_part')
    new_part_id = fields.Many2one('comodel_name', string='new_part')


class Parts(models.Model):
    _name = "ws.parts"
    _description = "Part Model"
    name = fields.Char('name')
    manufacturer = fields.Char('manufacturer')
    price = fields.Float('price')
