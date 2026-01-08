from odoo import models, fields, api


class HospitalDiagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'Diagnóstico Médico'
    _rec_name = 'diagnostico_historial'

    paciente_id = fields.Many2one("hospital.paciente", string="Paciente", required=True)
    medico_id = fields.Many2one("hospital.medico", string="Médico", required=True)
    diagnostico = fields.Text(string="Diagnóstico", required=True)

    diagnostico_historial = fields.Char(string="Historial", compute="_compute_diagnostico_historial", store=True)

    @api.depends('paciente_id', 'medico_id', 'diagnostico')
    def _compute_diagnostico_historial(self):
        for record in self:
            record.diagnostico_historial = f"Paciente: {record.paciente_id.name}, Médico: {record.medico_id.name}, Diagnóstico: {record.diagnostico}"
