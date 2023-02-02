# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
    _name = 'dm.ooddle.users'
    user_id = fields.Integer('id', required=True, help="Introduce el id del cliente")
    mobile = fields.Integer('mobile', required=True)
    points = fields.Integer( 'points', help = "Introduce los puntos que tiene el jugardor en la liga")
    league = fields.Char( 'league')
    mail = fields.Char( 'mail', required=True)


class UserResgistered(models.Model):
    _name = 'dm.ooddle.usersregistered'
    user_registered = fields.Many2one('dm.ooddle.users','user_id', help= "Introduce el usuario que jugara el partido")
    matches_ids = fields.Many2many('dm.ooddle.matches','match_id', help= 'Introduce el partido nuevo')


class Matches(models.Model):
    _name = 'dm.ooddle.matches'
    match_id = fields.Integer( 'match_id', required=True, help = "Introduce el id del partido")
    court = fields.Many2one('dm.ooddle.courts','court_id',required=True)
    time = fields.Datetime('time', required=True, help= 'indica la fecha del partido')

class Courts(models.Model):
    _name = 'dm.ooddle.courts'
    court_id= fields.Integer('court_id', required=True, help = 'Introduce el id de la pista')
    place = fields.Char('place', required=True, help = 'Introduce el lugar de la pista')
    used = fields.Boolean( 'used', default = False, help = 'La pista esta en uso')
        