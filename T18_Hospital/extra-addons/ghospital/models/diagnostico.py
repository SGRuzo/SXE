from odoo import models, fields, api


class HospitalDiagnostico(models.Model):
    _name = 'ghospital.diagnostico'
    _description = 'Diagnóstico Médico'
    _rec_name = 'diagnostico_historial'

    id_paciente = fields.Many2one("ghospital.paciente", string="Paciente", required=True)
    id_medico = fields.Many2one("ghospital.medico", string="Médico", required=True)
    diagnostico = fields.Text(string="Diagnóstico", required=True)

    diagnostico_historial = fields.Char(string="Historial", compute="_compute_diagnostico_historial", store=True)

    @api.depends('id_paciente', 'id_medico', 'diagnostico')
    def _compute_diagnostico_historial(self):
        for record in self:
            paciente_name = record.id_paciente.name if record.id_paciente else "Sin paciente"
            medico_name = record.id_medico.name if record.id_medico else "Sin médico"
            diagnostico_text = record.diagnostico if record.diagnostico else "Sin diagnóstico"
            record.diagnostico_historial = f"Paciente: {paciente_name}, Médico: {medico_name}, Diagnóstico: {diagnostico_text}"
