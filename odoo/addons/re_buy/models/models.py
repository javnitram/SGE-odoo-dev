# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rebuyEmployees(models.Model):
    _name = 'am.rebuy.employees'
    name = fields.Char('Name')
    employee_product_sold = fields.One2many('am.rebuy.products', 'product_employee', string='Products sold')
    
class rebuyProducts(models.Model):
    _name = 'am.rebuy.products'
    name = fields.Char('Name', help = "Insert product name")
    product_price = fields.Float('Price', help = "Insert product price")
    product_stock = fields.Integer('Stock', help = "Insert product stock")
    product_grade = fields.Char('Grade', help = "Insert product grade")
    product_employee = fields.Many2one('am.rebuy.employees', string='Employee')
    product_client = fields.Many2one('am.rebuy.client', string='Client')
    client_ids = fields.Many2many('am.rebuy.client', string='Pre-order client')
    product_check_grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string='product_check_grade') 

class rebuyClient(models.Model):
    _name = 'am.rebuy.client'
    name = fields.Char('Name')
    client_fidelity_number = fields.Char('Fidelity card number')
    client_product_sold = fields.One2many('am.rebuy.client_products', 'client_product_client', string='Sold products')
    client_product_bought = fields.One2many('am.rebuy.products', 'product_client', string='Bought products')
    preorder_ids = fields.Many2many('am.rebuy.products', string='Pre-orders')

class rebuyClientProducts(models.Model):
    _name = 'am.rebuy.client_products'
    name = fields.Char('Name', help = "Insert product name")
    client_product_price = fields.Float('Price', help = "Insert product price")
    client_product_stock = fields.Integer('Stock', help = "Insert product stock")
    client_product_grade = fields.Char('Grade', help = "Insert product grade")
    client_product_employee = fields.Many2one('am.rebuy.employees', string="Employee", help="Enter employee name")
    client_product_client = fields.Many2one('am.rebuy.client', string='Client', help="Enter client name")
    client_product_accepted = fields.Boolean('Accepted', help = "Enter if accepted")
    stage_id = fields.Many2one('am.rebuy.stages', string='stage')
    client_product_check_grade = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ], string='client_product_check_grade') 

class rebuyStages(models.Model):
    _name = 'am.rebuy.stages'
    client_product_stage_new = fields.Char('New', help = "Insert stage")
    client_product_stage_checking = fields.Char('Checking', help = "Insert stage")
    client_product_stage_approved = fields.Char('Approved', help = "Insert stage")
    client_product_stage_completed = fields.Char('Completed', help = "Insert stage")
    product_stage_ids = fields.One2many('am.rebuy.client_products', 'stage_id', string='products')
