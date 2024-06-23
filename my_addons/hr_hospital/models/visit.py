from odoo import models, fields

class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    date = fields.Date(string='Date')
    reason = fields.Text(string='Reason')
