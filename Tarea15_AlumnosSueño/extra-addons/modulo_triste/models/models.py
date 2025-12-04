# -*- coding: utf-8 -*-

from odoo import models, fields, api

class modulo_triste(models.Model):
    _name = 'modulo_triste.modulo_triste'
    _description = 'Recomendación de Bebida Anti-Sueño'

    alumno = fields.Char(required=True)
    nivel_sueno = fields.Integer(string='Nivel de Sueño (1-10)', required=True, default=1)
    bebida_recomendada = fields.Char(compute='_calcular_bebida_recomendada', store=True)

    @api.depends('nivel_sueno')
    def _calcular_bebida_recomendada(self):
        for record in self:
            nivel = record.nivel_sueno

            if nivel < 1:
                record.nivel_sueno = 1
                nivel = 1
            elif nivel > 10:
                record.nivel_sueno = 10
                nivel = 10

            if 1 <= nivel <= 3:
                record.bebida_recomendada = 'Café con leche'
            elif 4 <= nivel <= 6:
                record.bebida_recomendada = 'Café solo largo'
            elif 7 <= nivel <= 9:
                record.bebida_recomendada = 'Café solo larguísimo'
            elif nivel == 10:
                record.bebida_recomendada = 'Inyección de adrenalina'
            else:
                record.bebida_recomendada = 'Nivel de sueño inválido'

