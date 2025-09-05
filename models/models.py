# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError

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
    
class EmployeePublic(models.Model):
    _inherit ='hr.employee.public'

    branch_id = fields.Many2one('branches',string='Employee Branch')
    


class ResUsers(models.Model):

    _inherit = "res.users"

    is_manager_access = fields.Boolean(string="Inventory Manager")
    
    
class UoM(models.Model):
    _inherit = "uom.uom"

    # @api.model
    # def create(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to create new UOM.'),
    #         )
    #     else:
    #         return super(UoM, self).create(vals)


    # def write(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to update UOM.'),
    #         )
    #     else:
    #         return super(UoM, self).write(vals)


class UoMCategory(models.Model):
    _inherit = "uom.category"

    # @api.model
    # def create(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to create new UOM.'),
    #         )
    #     else:
    #         return super(UoMCategory, self).create(vals)

    # def write(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to update  UOM.'),
    #         )
        # else:
        #     return super(UoMCategory, self).write(vals)
    



class ProductTemplate(models.Model):
    
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        if self.env.user.is_manager_access != True:
            raise UserError(
                _('Sorry, you are not allowed to create new product.'),
            )
        else:
            return super(ProductTemplate, self).create(vals)
    
    
    def write(self, vals):
        # Check if the user has is_manager_access=True
        if not self.env.user.is_manager_access:
            # Check if name or default_code is being modified
            restricted_fields = ['name', 'default_code']
            modified_restricted_fields = [field for field in restricted_fields if field in vals]
            if modified_restricted_fields:
                raise UserError(
                    _('Sorry, you are not allowed to edit the following fields: %s.') % ', '.join(modified_restricted_fields)
                )
        return super(ProductTemplate, self).write(vals)

class Product(models.Model):
    
    _inherit = 'product.product'
 
    @api.model
    def create(self, vals):
        if not self.env.user.is_manager_access:
            raise UserError(_('Sorry, you are not allowed to create new product.'))
        return super().create(vals)

    def write(self, vals):
        if not self.env.user.is_manager_access:
            restricted_fields = ['name', 'default_code']
            modified_restricted_fields = [field for field in restricted_fields if field in vals]
            if modified_restricted_fields:
                raise UserError(
                    _('Sorry, you are not allowed to edit the following fields: %s.') % ', '.join(modified_restricted_fields)
                )
        return super().write(vals)
    

    
    
class ResPartner(models.Model):

    _inherit = "res.partner"
    
    
    # @api.model
    # def create(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to create new partner.'),
    #         )
    #     else:
    #         return super(ResPartner, self).create(vals)

    # def write(self, vals):
    #     if self.env.user.is_manager_access != True:
    #         raise UserError(
    #             _('Sorry, you are not allowed to update  partner.'),
    #         )
    #     else:
    #         return super(ResPartner, self).write(vals)

    