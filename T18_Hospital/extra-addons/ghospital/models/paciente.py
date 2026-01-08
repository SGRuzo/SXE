from odoo import models, fields, api


class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Gestion Hospital Paciente'
    _rec_name = 'name'

    name = fields.Char(string="Nombre y apellido del Paciente", required=True)
    sintomas = fields.Text(string="Sintomas del Paciente")

    ids_diagnosticos  = fields.One2many("hospital.diagnostico", "paciente_id", string="Diagnósticos del Paciente")

