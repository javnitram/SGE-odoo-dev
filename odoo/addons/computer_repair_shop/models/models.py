# -*- coding: utf-8 -*-

from odoo import models, fields

class Clients(models.Model):
    _name = "ws.clients"
    _description = "Clients Model"
    name = fields.Char('name')
    phone = fields.Char('phone')
    email = fields.Char('email')


class Technicians(models.Model):
    _name = "ws.technicians"
    _description = "Technician Model"

    name = fields.Char('name')
    photo = fields.Image('photo')


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
        ('completed', 'Completed'),
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


class Motherboards(models.Model):
    _name = "ws.motherboards"
    _description = "Motherboards Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    size = fields.Selection([
        ('atx', 'ATX'),
        ('micro-atx', 'Micro ATX'),
        ('mini-itx', 'Mini ITX'),
    ], string='size')
    socket = fields.Char('socket')
    chipset = fields.Char('chipset')
    description = fields.Text('description')


class RAM(models.Model):
    _name = "ws.ram"
    _description = "RAM Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    capacity = fields.Char('capacity')


class CPU(models.Model):
    _name = "ws.cpu"
    _description = "CPU Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    socket = fields.Char('socket')
    architecture = fields.Char('architecture')
    number_of_cores = fields.Integer('number_of_cores')


class GPU(models.Model):
    _name = "ws.gpu"
    _description = "GPU Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    die = fields.Char('die')
    number_of_cores = fields.Integer('number_of_cores')
    vram = fields.Integer('vram')


class PSU(models.Model):
    _name = "ws.psu"
    _description = "PSU Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    power = fields.Integer('power')
    modular = fields.Selection([
        ('non_modular', 'Non modular'),
        ('semi_modular', 'Semi modular'),
        ('full_modular', 'Full modular'),
    ], string='modular')
    description = fields.Text('description')


class Chassis(models.Model):
    _name = "ws.chassis"
    _description = "Chassis Model"
    name = fields.Char('name')
    manufacturer = fields.Char('manufacturer')
    description = fields.Text('description')