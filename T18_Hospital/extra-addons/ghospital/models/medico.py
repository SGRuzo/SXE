from odoo import models, fields, api


class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Gestion Hospital Medico'
    _rec_name = 'name'

    name = fields.Char(string="Nombre y apellido del Médico", required=True)
    numero_colegiado = fields.Char(string="Número de Colegiado", required=True)

    ids_diagnosticos  = fields.One2many("hospital.diagnostico", "medico_id", string="Diagnósticos del Médico")