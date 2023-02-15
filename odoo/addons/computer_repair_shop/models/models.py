# -*- coding: utf-8 -*-

from odoo import models, fields

class Technician(models.Model):
    _name = "ws.technician"
    _description = "Technician Model"

    name = fields.Char('name')
    photo = fields.Image('photo', max_width=512, max_height=512)


class Repairment(models.Model):
    _name = 'ws.repairment'
    _description = 'Repair Model'
    repair_status = fields.Selection([
        ('quote', 'Presupuesto'),
        ('accepted', "Aceptado"),
        ('processing', "En proceso"),
        ('ready', 'Listo')
    ], string='repair_status')
    start_date = fields.Date('start_date')
    completion_date = fields.Date('completion_date')
    labor_cost = fields.Float('labor_cost')


class Replacement(models.Model):
    _name = "ws.replacement"
    _description = "Replacement Model"
    old_part_id = fields.Many2one('comodel_name', string='old_part')
    new_part_id = fields.Many2one('comodel_name', string='new_part')


class Part(models.Model):
    _name = "ws.part"
    _description = "Part Model"
    name = fields.Char('name')
    manufacturer = fields.Char('manufacturer')
    price = fields.Float('price')
