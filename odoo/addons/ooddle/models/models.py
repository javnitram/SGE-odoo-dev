# -*- coding: utf-8 -*-

from odoo import _, models, fields,api
from odoo.exceptions import ValidationError
from lxml import etree
import base64



class Users(models.Model):
    _name = 'dm.ooddle.users'
    _description='Users'
    name = fields.Char('Name')
    mobile = fields.Integer('Mobile', required=True)
    points = fields.Integer( 'Points', help = "Introduce los puntos que tiene el jugardor en la liga")
    league = fields.Char( 'League')
    mail = fields.Char( 'Mail', required=True)
    image = fields.Image('Image')
    teams_ids= fields.Many2many('dm.ooddle.teams', string='Team')
    
class Teams(models.Model):
    _name = 'dm.ooddle.teams'
    _description = 'Teams'
    name = fields.Char('Name', required=True)
    users_ids = fields.Many2many('dm.ooddle.users',string='Users')
    matches_ids = fields.Many2many('dm.ooddle.matches', string='Matches')
    image = fields.Image('image')
    @api.model_create_single
    def create(self, vals):
        if vals.get('users_ids'):
            if len(vals.get('users_ids'))>2:
                raise ValidationError(_("Error there can only be two users per team"))
        return super().create(vals)
    
    @api.constrains('users_ids')
    def _more_than_two(self):
        if len(self.users_ids)>2:
            raise ValidationError(_("Error there can only be two users per team"))
    
    #@api.onchange('image')
    #def _change_image(self):
        #if self.matches_ids:
         #   for record in self.matches_ids:
          #      if record.team_ids[0].id ==self.id:
          #          record.image_team1 = self.image
           #     elif record.team_ids[1].id ==self.id:
            #        record.image_team2 = self.image

class Matches(models.Model):
    _name = 'dm.ooddle.matches'
    _description='Matches'
    name = fields.Char('Name',required=True)
    team_ids = fields.Many2many('dm.ooddle.teams',string='Teams Registered')
    court = fields.Many2one('dm.ooddle.courts','Court',required=True)
    time = fields.Date(string='Time', required=True, help= 'Indicate the date of the match')
    price = fields.Float('price')


    
    #def _read_image(self):
     #   with open('default.png','rb') as img:
      #      image = base64.b64encode(img.read())
       # return image
    
    image_team1 = fields.Image('image_team1')
    image_team2 = fields.Image('image_team2')
    state = fields.Selection([('open', 'Open'), ('close', 'Close'), ('playing', 'In game'), ('done', 'Finished')],
        string='Status', required=True, default = 'open',tracking=True,copy=False,group_expand='_group_expand_states')
    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    
    
    #@api.model
    #def fields_view_get(self, view_id=None, view_type='kanban', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id, view_type, toolbar, submenu)
        if view_type == 'kanban':
            doc = etree.XML(res['arch'])
            name_field = doc.xpath("//field[@name='time']")
            if name_field:
                if self.image_team1 !=None:
                    name_field[0].addnext(etree.Element('field', {'name': 'name'}))
                    res['arch']= etree.tostring(doc, encoding='unicode')
        return res

    @api.onchange('team_ids')
    def _next_state(self):
        if len(self.team_ids) == 0:
            self.image_team1 = None
            self.image_team2 = None
        elif len(self.team_ids) ==1:
            self.image_team1 = self.team_ids[0].image
            self.image_team2 = None
        elif len(self.team_ids) == 2:
            self.image_team1 = self.team_ids[0].image
            self.image_team2 = self.team_ids[1].image
            self.state = 'close'

    @api.model_create_single
    def create(self, vals):
        if len(self.team_ids) == 0:
            self.image_team1 = None
            self.image_team2 = None
        elif len(self.team_ids) ==1:
            self.image_team1 = self.team_ids[0].image
            self.image_team2 = None
        elif len(self.team_ids) == 2:
            self.image_team1 = self.team_ids[0].image
            self.image_team2 = self.team_ids[1].image
            self.state = 'close'

        return super().create(vals)
   
    @api.constrains('team_ids')
    def _more_than_two(self):
        if len(self.team_ids)>2:
            raise ValidationError(_("Error there can only be two teams per game"))
     

class Courts(models.Model):
    _name = 'dm.ooddle.courts'
    _description='Courts'
    name = fields.Char('Name')
    match_ids = fields.One2many('dm.ooddle.matches', 'court', string='match')
    place = fields.Char('Place', required=True, help = 'Enter the location of the court')
    in_use = fields.Boolean( 'In use', default = False, help = 'Check if the court is in use')

    

