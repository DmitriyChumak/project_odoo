from odoo import models, fields

class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Doctor'

    name = fields.Char(string='Name', required=True)
    specialization = fields.Char(string='Specialization')
    patient_ids = fields.One2many('hr_hospital.patient', 'doctor_id', string='Patients')
