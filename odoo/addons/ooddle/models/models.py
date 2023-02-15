# -*- coding: utf-8 -*-

from odoo import _, models, fields, api
from odoo.exceptions import ValidationError

class Users(models.Model):
    _name = 'dm.ooddle.users'
    name = fields.Char('Name')
    mobile = fields.Integer('Mobile', required=True)
    points = fields.Integer( 'Points', help = "Introduce los puntos que tiene el jugardor en la liga")
    league = fields.Char( 'League')
    mail = fields.Char( 'Mail', required=True)
    image = fields.Image('Image')
    team_id = fields.Many2one('dm.ooddle.teams', string='Team')
    
class Teams(models.Model):
    _name = 'dm.ooddle.teams'
    _description = 'Equipos'
    name = fields.Char('Name')
    users_ids = fields.One2many('dm.ooddle.users', 'team_id', string='Users')
    matches_ids = fields.Many2many('dm.ooddle.matches', string='Matches')
    @api.model_create_single
    def create(self, vals):
        if len(vals.get('users_ids'))>2:
            raise ValidationError(_("Error solo puede haber dos jugadores por equipo"))
        return super().create(vals)
    
    def write(self, vals):
        if len(vals.get('users_ids'))>2:
            raise ValidationError(_("Error solo puede haber dos jugadores por equipo"))
        return super().write(vals)
    
class Matches(models.Model):
    _name = 'dm.ooddle.matches'
    name = fields.Char('Name',required=True)
    team_ids = fields.Many2many('dm.ooddle.teams',relation='dm_ooddle_teams_match',string='Teams Registered')
    court = fields.Many2one('dm.ooddle.courts','Court',required=True)
    time = fields.Datetime(string='Time', required=True, help= 'indica la fecha del partido')
    price = fields.Float('price')
    stage_ids = fields.Many2many('dm.ooddle.match.stages', string='stage')
    
    @api.constrains('Matches')
    def _more_than_two(self):
        if len(Matches.team_ids)>2:
            raise ValidationError(_("Error solo puede haber dos equipos por partidos"))
     

class Courts(models.Model):
    _name = 'dm.ooddle.courts'
    name = fields.Char('Name')
    match_ids = fields.One2many('dm.ooddle.matches', 'court', string='match')
    place = fields.Char('Place', required=True, help = 'Introduce el lugar de la pista')
    in_use = fields.Boolean( 'In use', default = False, help = 'La pista esta en uso')

class TournamentStates(models.Model):
    _name = 'dm.ooddle.match.states'
    _description = 'Etapas del partido en el torneo'
    name = fields.Char('Name')
    finished = fields.Boolean('finished' ,default ='False')
    match_id = fields.Many2many('dm.ooddle.match', string='match')


