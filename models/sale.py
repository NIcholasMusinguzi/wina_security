
from odoo import models, fields, api

class WinaSaleOrder(models.Model):
    _inherit = 'sale.order'


    def default_get(self, fields):
        res = super(WinaSaleOrder, self).default_get(fields)
        emplo = self.env['hr.employee'].search([('user_id','=',self.env.user.id)], limit=1)
        if emplo and emplo.branch_id:
            res['branch_id'] = emplo.branch_id.id
        return res

    branch_id = fields.Many2one('branches',string="branch")




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def default_get(self, fields):
        res = super(SaleOrderLine, self).default_get(fields)
        emplo = self.env['hr.employee'].search([('user_id','=',self.env.user.id)], limit=1)
        warehouse = self.env['stock.warehouse'].search(
            [('company_id', '=', self.env.user.company_id.id)], limit=1)
        if emplo and emplo.branch_id.location_id.id:
            
            res['location_id'] = emplo and \
                emplo.branch_id.location_id.id or False
        else:
            res['location_id'] = warehouse and \
                warehouse.lot_stock_id.id or False
        return res

    location_id = fields.Many2one('stock.location', string="Location",
                                  domain="[('usage','=','internal')]")

    
class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(
            self, product_id, product_qty, product_uom, location_id,
            name, origin, company_id, values):
        if values.get('sale_line_id', False):
            sale_line_id = self.env['sale.order.line'].sudo().browse(
                values['sale_line_id'])
            if sale_line_id.location_id:
                self.location_src_id = sale_line_id.location_id.id
            else:
                self.location_src_id = self.picking_type_id.default_location_src_id.id
        return super(StockRule, self)._get_stock_move_values(
            product_id, product_qty, product_uom, location_id,
            name, origin, company_id, values)
