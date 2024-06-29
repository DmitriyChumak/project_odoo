# visit model

from odoo import models, fields

class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    patient_id = fields.Many2one('hr_hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor', required=True)
    disease_id = fields.Many2one('hr_hospital.disease', string='Disease', required=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    symptoms = fields.Text(string='Symptoms')
    notes = fields.Text(string='Notes')
