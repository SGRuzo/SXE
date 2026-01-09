from odoo import models, fields, api


class HospitalPaciente(models.Model):
    _name = 'ghospital.paciente'
    _description = 'Gestion Hospital Paciente'
    _rec_name = 'name'

    name = fields.Char(string="Nombre y apellido del Paciente", required=True)
    sintomas = fields.Text(string="Sintomas del Paciente")

    id_diagnostico  = fields.One2many("ghospital.diagnostico", "id_paciente", string="Diagnósticos del Paciente")

