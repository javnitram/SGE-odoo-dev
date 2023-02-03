# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rebuyEmployee(models.Model):
    _name = 'am.rebuy.employees'
    description = fields.Text(string="Rebuy Employees ")
    emp_name = fields.Char('Name', help="Insert name")
    
class rebuyProduct(models.Model):
    _name = 'am.rebuy.product'
    product_name = fields.Char('Name', help = "Insert product name")
    product_price = fields.Float('Price', help = "Insert product price")
    product_stock = fields.Integer('Stock', help = "Insert product stock")
    product_grade = fields.Char('Grade', help = "Insert product grade")
    client_product_employee = fields.Many2one('Employee')
    client_product_client = fields.Many2one('Client')
    product_check_grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string='product_check_grade') 

class rebuyClient(models.Model):
    _name = 'am.rebuy.client'
    client_name = fields.Char('Name', help = "Enter client name")
    client_fidelity_number = fields.Integer('Fidelity card number')

class rebuyClientProduct(models.Model):
    _name = 'am.rebuy.clientproduct'
    client_product_name = fields.Char('Name', help = "Insert product name")
    client_product_price = fields.Float('Price', help = "Insert product price")
    client_product_stock = fields.Integer('Stock', help = "Insert product stock")
    client_product_grade = fields.Char('Grade', help = "Insert product grade")
    client_product_employee = fields.Many2one('Employee')
    client_product_client = fields.Many2one('Client')
    client_product_accepted = fields.Boolean('Accepted', help = "Enter if accepted")
    client_product_check_grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string='client_product_check_grade') 