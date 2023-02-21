# -*- coding: utf-8 -*-
import datetime

from odoo import models, fields, api


class golosinas(models.Model):
     _name = 'wb.golosy.golosinas'
     _description = 'Nombre y lista de golosinas'

     name = fields.Char('Nombre', required=True, help='Nombre de la golosina')
     precio = fields.Float('Precio', required=True, help='precio de la golosina')
     cantidad = fields.Integer('Cantidad', required=True, help='Cantidad stock de la golosina')
     description = fields.Text()
     active = fields.Boolean(string ='¿Esta colocada en la tienda?', default=False, help='Golosina colocada o no')
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
     golosinas_ids = fields.One2many('wb.golosy.golosinas', 'categoria_id', string='Golosinas')
     
class Camion(models.Model):
     _name = 'wb.golosy.camion'
     _description = 'Camion envio a domicilio'

     name = fields.Char('Matricula', required=True, help='Matricula del camión')
     golosinas2_ids = fields.Many2many('wb.golosy.golosinas', string=' Camion de pedido')
     empleado_id = fields.Many2one("wb.golosy.empleados",string=" Empleados",required=True,ondelete="cascade")
     productos = fields.Char('Productos')#compute="_productoscamion")
     

class Empleados(models.Model):
     _name = 'wb.golosy.empleados'
     _description = 'Empleados de golosy'

     name = fields.Char('Nombre', required=True, help='Nombre del empleado')
     dni = fields.Char('DNI', required=True, help='DNI del empleado')
     telefono = fields.Integer('Telèfono', required=True, help='Telèfono del empleado')
     antiguedad = fields.Date('Fecha de incorporacion', required=True, help='Fecha de primer dia de trabajo')
     camiones_ids = fields.One2many('wb.golosy.camion', 'empleado_id', string=' camion')
     imagen = fields.Image(string='Imagen', help='Imagen del empleado')
     mesestrabajados = fields.Char('Meses de trabajo en la empresa', compute="_mesestrabajados")
     
     def _mesestrabajados(self):
          fecha_hoy = datetime.date.today()
          for empl in self:
               if empl.antiguedad:
                    antiguedad = fields.Datetime.to_datetime(empl.antiguedad).date()
                    total_meses = str(int((fecha_hoy - antiguedad).days/30))
                    empl.mesestrabajados = total_meses
               else:
                    empl.mesestrabajados = "no hay registro"