

from odoo import models, fields, api


class ejercito(models.Model):
    _name = 'ac.reclutamiento.ejercito'
    _description = 'ac.reclutamiento.ejercito'
    nombre = fields.Char()
    unidades= fields.Integer()
    campanas = fields.Many2many('ac.reclutamiento.campana', string='Campañas en las que participan')
    general = fields.Many2one('ac.reclutamiento.general', string='General que lo gestiona')
  

class general(models.Model):
    _name = 'ac.reclutamiento.general'
    _description = 'ac.reclutamiento.general'
    imagen= fields.Image(string="imagen",store=True,relation="res.partner",help="Inserte la imagen aqui")
    name = fields.Char(string="nombre del general")
    edad= fields.Integer() 
    ejercitos_gestionados = fields.One2many('ac.reclutamiento.ejercito', inverse_name='general', string='ejercitos_gesionados')
  
  


class infanteria_CaC(models.Model):
    _name = 'ac.reclutamiento.infanteria.cac'
    _description = 'ac.reclutamiento.infanteria.cac'
    nombre = fields.Char()
    descripcion = fields.Text()
    armadura = fields.Selection([
        ('1', 'Ligera')
        ,('2','Media')
        ,('3','Pesada')
    ], string='armadura')

class infanteria_proyectiles(models.Model):
    _name = 'ac.reclutamiento.infanteria.proyectiles'
    _description = 'ac.reclutamiento.infanteria.proyectiles'
    nombre = fields.Char()
    descripcion = fields.Text()
    municion= fields.Selection([
        ('1','Piedras'),
        ('2','Flechas'),
        ('3','Jabalinas')
    ], string='municion')
    alcance= fields.Integer()
    alcanceEnPies=fields.Float(string="Alcance en pies ",compute="_alcanceEnPies", store=True)
    @api.depends('alcance')
    def _alcanceEnPies(self):
        for i in self:
            i.alcanceEnPies=i.alcance*3.3
    


class undiades_motadas(models.Model):
    _name = 'ac.reclutamiento.unidades.montadas'
    _description = 'ac.reclutamiento.unidades.montadas'
    nombre = fields.Char()
    descripcion = fields.Text()
    monturas = fields.Selection([
        ('1', 'Caballo'),
        ('2','Camello'),
        ('3','Elefante')
    ], string='monturas')
    velocidad= fields.Integer()
    


    
class artilleria(models.Model):
    _name = 'ac.reclutamiento.artilleria'
    _description = 'ac.reclutamiento.artilleria' 
    nombre = fields.Char()
    descripcion = fields.Text()
    municion = fields.Selection([
        ('1', 'piedra'),
        ('2','virote')
    ], string='municion')    
    alcance= fields.Integer()
    alcanceEnPies=fields.Float(string="Alcance en pies ",compute="_alcanceEnPies", store=True)
    @api.depends('alcance')
    def _alcanceEnPies(self):
        for i in self:
            i.alcanceEnPies=i.alcance*3.3
    

class campana(models.Model):
    _name = 'ac.reclutamiento.campana'
    _description = 'ac.reclutamiento.campana'
    nombre = fields.Char()
    pais_id = fields.Many2one('res.country', string='Pais')
    fecha_inicio= fields.Date()
    ejercitos = fields.Many2many(comodel_name='ac.reclutamiento.ejercito', string='Ejercitos que participan')
