# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
    _name = 'dm.ooddle.users'
    name = fields.Char('name')
    mobile = fields.Integer('mobile', required=True)
    points = fields.Integer( 'points', help = "Introduce los puntos que tiene el jugardor en la liga")
    league = fields.Char( 'league')
    mail = fields.Char( 'mail', required=True)
    image = fields.Image('image')

class UserResgistered(models.Model):
    _name = 'dm.ooddle.usersregistered'
    user_registered = fields.Many2one('dm.ooddle.users','user_id', help= "Introduce el usuario que jugara el partido")
    match = fields.Many2many('dm.ooddle.matches','match_id', help= 'Introduce el partido nuevo')

class Matches(models.Model):
    _name = 'dm.ooddle.matches'
    court = fields.Many2one('dm.ooddle.courts','court_id',required=True)
    time = fields.Datetime('time', required=True, help= 'indica la fecha del partido')
    price = fields.Float('price', required=True)

class Courts(models.Model):
    _name = 'dm.ooddle.courts'
    match_ids = fields.One2many('dm.ooddle.matches', 'court', string='indica el partido que se jugara en esa vista')
    place = fields.Char('place', required=True, help = 'Introduce el lugar de la pista')
    used = fields.Boolean( 'used', default = False, help = 'La pista esta en uso')

