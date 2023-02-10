# -*- coding: utf-8 -*-

from odoo import models, fields

class Repair(models.Model):
    _name = 'ws.repair'
    _description = 'Repair Model'

    repair_status = fields.Integer('repair_status')
