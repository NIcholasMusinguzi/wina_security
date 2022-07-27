# -*- coding: utf-8 -*-
# from odoo import http


# class WinaSecurity(http.Controller):
#     @http.route('/wina_security/wina_security/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wina_security/wina_security/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wina_security.listing', {
#             'root': '/wina_security/wina_security',
#             'objects': http.request.env['wina_security.wina_security'].search([]),
#         })

#     @http.route('/wina_security/wina_security/objects/<model("wina_security.wina_security"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wina_security.object', {
#             'object': obj
#         })
