from odoo import models, fields, api


class HospitalMedico(models.Model):
    _name = 'ghospital.medico'
    _description = 'Gestion Hospital Medico'
    _rec_name = 'name'

    name = fields.Char(string="Nombre y apellido del Médico", required=True)
    numero_colegiado = fields.Char(string="Número de Colegiado", required=True)

    id_diagnostico = fields.One2many("ghospital.diagnostico", "id_medico", string="Diagnósticos del Médico")
