# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Users(models.Model):
    _name = 'dm.ooddle.users'
    name = fields.Char('Name')
    mobile = fields.Integer('Mobile', required=True)
    points = fields.Integer( 'Points', help = "Introduce los puntos que tiene el jugardor en la liga")
    league = fields.Char( 'League')
    mail = fields.Char( 'Mail', required=True)
    image = fields.Image('Image')
    matches_ids = fields.Many2many('dm.ooddle.matches', string='Matches')

class Matches(models.Model):
    _name = 'dm.ooddle.matches'
    name = fields.Char('Name')
    users_ids = fields.Many2many('dm.ooddle.users', string='User Resgitered')
    court = fields.Many2one('dm.ooddle.courts','Court',required=True)
    time = fields.Datetime(string='Time', required=True, help= 'indica la fecha del partido')
    price = fields.Float(string= 'Price', required=True)
    stage_ids = fields.One2many('dm.ooddle.match.stages', 'match_id', string='stage')

class Courts(models.Model):
    _name = 'dm.ooddle.courts'
    name = fields.Char('Name')
    match_ids = fields.One2many('dm.ooddle.matches', 'court', string='')
    place = fields.Char('Place', required=True, help = 'Introduce el lugar de la pista')
    in_use = fields.Boolean( 'In use', default = False, help = 'La pista esta en uso')

class TournamentStages(models.Model):
    _name = 'dm.ooddle.match.stages'
    _description = 'Etapas del partido en el torneo'
    name = fields.Char('Name')
    finished = fields.Boolean('finished' ,default ='False')
    match_id = fields.Many2one('dm.ooddle.match', string='match')
    

