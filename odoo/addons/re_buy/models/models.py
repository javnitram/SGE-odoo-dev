# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class rebuyEmployees(models.Model):
    _name = 'am.rebuy.employees'
    name = fields.Char('Name')
    employee_product_sold = fields.One2many('am.rebuy.stock_sold', 'product_employee', string='Products sold')
    employee_product_bought = fields.One2many('am.rebuy.client_products', 'client_product_employee', string='Products bought')
    
class rebuyProducts(models.Model):
    _name = 'am.rebuy.products'
    description = fields.Text('Description')
    name = fields.Char('Name', help = "Insert product name")
    product_image = fields.Image('Image')
    stock_ids = fields.One2many('am.rebuy.stock', 'product_id', string='Stock')
    sold_ids = fields.One2many('am.rebuy.stock_sold', 'product_id', string='Sold')

    
class rebuyStock(models.Model):
    _name = 'am.rebuy.stock'
    product_id = fields.Many2one('am.rebuy.products', string='Product')
    product_price = fields.Float('Price', help = "Insert product price")
    product_stock = fields.Integer('Stock', help = "Insert product stock")
    product_grade = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string='Grade')
    product_employee = fields.Many2one('am.rebuy.employees', string='Seller')
    product_client = fields.Many2one('am.rebuy.clients', string='Buyer')
    product_reserved = fields.Many2many('am.rebuy.clients', string='Reservation')

    def sell_stock(self):
        for record in self:
            product_obj = self.env['am.rebuy.stock_sold']
            product_obj_delete = self.env['am.rebuy.stock']
            defaults = {
                'product_id': record.product_id.id,
                'product_price': record.product_price,
                'product_stock': record.product_stock,
                'product_grade': record.product_grade,
                'product_employee': record.product_employee.id,
                'product_client': record.product_client.id,
                'product_sold_date': date.today(),
            }
            product_obj.create(defaults)
            product_obj_delete.search([('id','=', self.id)]).unlink()

class rebuyStockSold(models.Model):
    _inherit = 'am.rebuy.stock'
    _name = 'am.rebuy.stock_sold'
    product_id = fields.Many2one('am.rebuy.products', string='Product')
    product_price = fields.Float('Price', help = "Insert product price")
    product_stock = fields.Integer('Stock', help = "Insert product stock")
    product_grade = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C')], string='Grade')
    product_employee = fields.Many2one('am.rebuy.employees', string='Seller')
    product_client = fields.Many2one('am.rebuy.clients', string='Buyer')
    product_sold_date = fields.Date('Selling date')

    def return_stock(self):
        for record in self:
            product_obj = self.env['am.rebuy.stock']
            product_obj_delete = self.env['am.rebuy.stock_sold']
            defaults = {
                'product_id': record.product_id.id,
                'product_price': record.product_price,
                'product_stock': record.product_stock,
                'product_grade': record.product_grade,
            }
            product_obj.create(defaults)
            product_obj_delete.search([('id','=', self.id)]).unlink()

class rebuyClients(models.Model):
    _name = 'am.rebuy.clients'
    name = fields.Char('Name')
    client_fidelity_number = fields.Char('Fidelity card number')
    client_product_sold = fields.One2many('am.rebuy.client_products', 'client_product_client', string='Sold products')
    client_product_bought = fields.One2many('am.rebuy.stock_sold', 'product_client', string='Bought products')
    client_reservation = fields.Many2many('am.rebuy.stock', string='Reservations')

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
