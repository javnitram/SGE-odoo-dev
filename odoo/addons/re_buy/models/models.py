# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rebuyEmployees(models.Model):
    _name = 'am.rebuy.employees'
    name = fields.Char('Name')
    employee_product_sold = fields.One2many('am.rebuy.stock', 'product_employee', string='Products sold')
    
class rebuyProducts(models.Model):
    _name = 'am.rebuy.products'
    description = fields.Text('Description')
    name = fields.Char('Name', help = "Insert product name")
    product_image = fields.Image('Image')
    stock_ids = fields.One2many('am.rebuy.stock', 'product_id', string='Stock')
    client_ids = fields.Many2many('am.rebuy.clients', string='Pre-order client')

class rebuyStock(models.Model):
    _name = 'am.rebuy.stock'
    product_id = fields.Many2one('am.rebuy.products', string='Product')
    product_price = fields.Float('Price', help = "Insert product price")
    product_stock = fields.Integer('Stock', help = "Insert product stock")
    product_grade = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string='Grade')
    product_employee = fields.Many2one('am.rebuy.employees', string='Seller')
    product_client = fields.Many2one('am.rebuy.clients', string='Buyer')

class rebuyClients(models.Model):
    _name = 'am.rebuy.clients'
    name = fields.Char('Name')
    client_fidelity_number = fields.Char('Fidelity card number')
    client_product_sold = fields.One2many('am.rebuy.client_products', 'client_product_client', string='Sold products')
    client_product_bought = fields.One2many('am.rebuy.stock', 'product_client', string='Bought products')
    preorder_ids = fields.Many2many('am.rebuy.stock', string='Pre-orders')

class rebuyClientProducts(models.Model):
    _name = 'am.rebuy.client_products'
    name = fields.Char('Name', help = "Insert product name")
    client_product_image = fields.Image('Image')
    client_product_price = fields.Float('Price', help = "Insert product price")
    client_product_stock = fields.Integer('Stock', help = "Insert product stock")
    client_product_grade = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string='Grade')
    client_product_employee = fields.Many2one('am.rebuy.employees', string="Employee", help="Enter employee name")
    client_product_client = fields.Many2one('am.rebuy.clients', string='Client', help="Enter client name")
    client_product_state = fields.Selection([('new', 'New'), ('checking', 'Checking'), ('checked', 'Checked'),('accepted', 'Accepted'),
    ('refused', 'Refused'),('completed', 'Completed'),('returned', 'Returned')], string='State')
    client_product_stage = fields.Selection([('new', 'New'), ('checking', 'Checking'), ('priced', 'Priced'), ('completed', 'Completed')],
    string='Stage', required=True, tracking=True, copy=False, group_expand='_expand_states')

    def _expand_states(self, sates, domain, order):
        return[key for key, val in type(self).client_product_stage.selection]
