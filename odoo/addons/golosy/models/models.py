# -*- coding: utf-8 -*-

from odoo import models, fields, api


class golosinas(models.Model):
     _name = 'wb.golosy.golosinas'
     _description = 'Nombre y lista de golosinas'

     name = fields.Char('Nombre', required=True, help='Nombre de la golosina')
     precio = fields.Float('Precio', required=True, help='precio de la golosina')
     cantidad = fields.Integer('Cantidad', required=True, help='Cantidad stock de la golosina')
     description = fields.Text()
     camion = fields.Selection([
        ('0', 'Solicitar al camión'),
        ('1', 'Dar de baja al producto')
     ], string='¿Solicitar al camion nuevo envio?')
     categoria_id = fields.Many2one("wb.golosy.categoria",string="Categoría",required=True,ondelete="cascade")
     imagen = fields.Image(string='Imagen', help='Imagen de la golosina')
     
class categorias(models.Model):
     _name = 'wb.golosy.categoria'
     _description = 'Categorias de las golosinas'

     name = fields.Char('Categoria', required=True, help='Nombre de la categoria')
     tipo = fields.Selection([
        ('0', 'Dulce'),
        ('1', 'Salado')
     ], string='Tipo de la categoria')
     golosinas_ids = fields.One2many('wb.golosy.golosinas', 'categoria_id', string='Categoria')
     
class Camion(models.Model):
     _name = 'wb.golosy.camion'
     _description = 'Camion envio a domicilio'

     name = fields.Char('Matricula', required=True, help='Matricula del camión')
     productos = fields.Integer('Productos', required=True, help='Productos a enviar')

class Empleados(models.Model):
     _name = 'wb.golosy.empleados'
     _description = 'Empleados de golosy'

     name = fields.Char('Nombre', required=True, help='Nombre del empleado')
     dni = fields.Char('DNI', required=True, help='DNI del empleado')
     telefono = fields.Integer('Telèfono', required=True, help='Telèfono del empleado')
     antiguedad = fields.Date('Antiguedad', required=True, help='Fecha de primer dia de trabajo')