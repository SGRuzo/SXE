# -*- coding: utf-8 -*-
# from odoo import http


# class Ghospital(http.Controller):
#     @http.route('/ghospital/ghospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ghospital/ghospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ghospital.listing', {
#             'root': '/ghospital/ghospital',
#             'objects': http.request.env['ghospital.ghospital'].search([]),
#         })

#     @http.route('/ghospital/ghospital/objects/<model("ghospital.ghospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ghospital.object', {
#             'object': obj
#         })

