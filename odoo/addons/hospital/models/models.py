# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HospitalDoctores(models.Model):
    _name="hospital.doctores"
    name=fields.Char(string ="Nombre",required=True,help="Introduce el nombre")

# class /mnt/extra-addons/hospital(models.Model):
#     _name = '/mnt/extra-addons/hospital./mnt/extra-addons/hospital'
#     _description = '/mnt/extra-addons/hospital./mnt/extra-addons/hospital'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
