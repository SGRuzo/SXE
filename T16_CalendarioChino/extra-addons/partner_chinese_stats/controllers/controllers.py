# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerChineseStats(http.Controller):
#     @http.route('/partner_chinese_stats/partner_chinese_stats', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_chinese_stats/partner_chinese_stats/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_chinese_stats.listing', {
#             'root': '/partner_chinese_stats/partner_chinese_stats',
#             'objects': http.request.env['partner_chinese_stats.partner_chinese_stats'].search([]),
#         })

#     @http.route('/partner_chinese_stats/partner_chinese_stats/objects/<model("partner_chinese_stats.partner_chinese_stats"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_chinese_stats.object', {
#             'object': obj
#         })

