# -*- coding: utf-8 -*-

from odoo import models, fields

class Clients(models.Model):
    _name = "ws.clients"
    _description = "Clients Model"
    name = fields.Char('name')
    phone = fields.Char('phone')
    email = fields.Char('email')
    computers_ids = fields.One2many('ws.computers', 'client_id', string='computers_ids')


class Technicians(models.Model):
    _name = "ws.technicians"
    _description = "Technician Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    repairments_ids = fields.Many2many('ws.repairments', string='repairments')


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
    cost = fields.Float('cost')
    computer_id = fields.Many2one('ws.computers', string='computer')
    issue_description = fields.Text('issue_description')
    technicians_ids = fields.Many2many('ws.technicians', string='technicians')


class Computers(models.Model):
    _name = "ws.computers"
    _description = "Computer model"
    motherboard_id = fields.Many2one('ws.motherboards', string='Motherboard')
    ram_id = fields.Many2one('ws.ram', string='RAM')
    cpu_id = fields.Many2one('ws.cpu', string='CPU')
    gpu_id = fields.Many2one('ws.gpu', string='GPU')
    psu_id = fields.Many2one('ws.psu', string='PSU')
    chassis_id = fields.Many2one('ws.chassis', string='Chassis')
    client_id = fields.Many2one('ws.clients', string='client')
    

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


class Chassis(models.Model):
    _name = "ws.chassis"
    _description = "Chassis Model"
    name = fields.Char('name')
    photo = fields.Image('photo')
    size = fields.Selection([
        ('atx', 'ATX'),
        ('micro-atx', 'Micro ATX'),
        ('mini-itx', 'Mini ITX'),
    ], string='size')