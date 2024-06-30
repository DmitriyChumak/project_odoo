from odoo import models, fields, api
from datetime import datetime, timedelta

class DiseaseReportWizard(models.TransientModel):
    _name = 'hr_hospital.disease.report.wizard'
    _description = 'Disease Report Wizard'

    doctor_ids = fields.Many2many('hr_hospital.doctor', string='Doctors')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')
    date_from = fields.Date(string='From', required=True, default=(datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
    date_to = fields.Date(string='To', required=True, default=datetime.now().strftime('%Y-%m-%d'))

    def action_generate_report(self):
        domain = [('date', '>=', self.date_from), ('date', '<=', self.date_to)]
        if self.doctor_ids:
            domain.append(('doctor_id', 'in', self.doctor_ids.ids))
        diagnoses = self.env['hr_hospital.diagnosis'].search(domain)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Disease Report',
            'res_model': 'hr_hospital.diagnosis',
            'view_mode': 'tree',
            'domain': [('id', 'in', diagnoses.ids)],
            'context': {'group_by': ['disease_id']},
        }
