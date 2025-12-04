# -*- coding: utf-8 -*-
from odoo import http


class Modulo_Triste(http.Controller):
    @http.route('/modulo_triste/modulo_triste', auth='public')
    def index(self, **kw):
       return "Hello, world"

    @http.route('/modulo_triste/modulo_triste/objects', auth='public')
    def list(self, **kw):
       return http.request.render('modulo_triste.listing', {
           'root': '/modulo_triste/modulo_triste',
           'objects': http.request.env['modulo_triste.modulo_triste'].search([]),
        })

    @http.route('/modulo_triste/modulo_triste/objects/<model("modulo_triste.modulo_triste"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('modulo_triste.object', {
            'object': obj
        })
