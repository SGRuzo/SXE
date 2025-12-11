# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

class PartnerChineseStats(models.Model):
    _inherit='res.partner'

    f_nac =fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string="Edad", readonly=True, compute='_calcular_edad', store=True)
    signo_chino =fields.Char(string="Signo Chino", readonly=True, compute='_calcular_chinada', store=True)
    codigo_socio = fields.Char(string="Código de Socio")
    nivel_fidelidad = fields.Selection(
        selection=[
            ('estandar', 'Estándar'),
            ('gold', 'Gold'),
            ('premium', 'Premium'),
        ],
        string="Nivel de Fidelidad",
        readonly=True,
        compute='_compute_nivel_fidelidad',
        store=True
    )
    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                today =date.today()
                record.edad = today.year-record.f_nac.year-((today.month, today.day)<(record.f_nac.month,record.f_nac.day))
            else:
                record.edad = 0

    @api.depends('f_nac')
    def _calcular_chinada(self):
        animales = ["Rata", "Buey", "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra", "Mono", "Gallo", "Perro", "Cerdo"]
        for record in self:
            if record.f_nac:
                year=record.f_nac.year
                index=(year - 1900) % 12 #12años es el tiempo de un ciclo chino
                record.signo_chino =animales[index]
            else:
                record.signo_chino="Sin signo"

    @api.depends('codigo_socio')
    def _compute_nivel_fidelidad(self):
        for record in self:
            if not record.codigo_socio:
                record.nivel_fidelidad='estándar'
            elif record.codigo_socio.upper().startswith('G'):
                record.nivel_fidelidad='gold'
            else:
                record.nivel_fidelidad='premium'
