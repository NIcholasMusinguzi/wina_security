# -*- coding: utf-8 -*-

from odoo import models, fields, api

class branches(models.Model):
    _name = 'branches'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    _description = 'Branches'
    _order = 'name asc'

    name = fields.Char(string="Branch Name", required=True)
    branch_code = fields.Char(string="Branch Code", required=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email")
    address = fields.Text(string="Address", required=True)    
    manager_id = fields.Many2one('res.users', string='Centre Head',)
    location_id = fields.Many2one('stock.location', 'Branch Stock Location')

    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         "The Branch name must be unique")
    ]

class Employee(models.Model):
    _inherit ='hr.employee'

    branch_id = fields.Many2one('branches',string='Employee Branch')