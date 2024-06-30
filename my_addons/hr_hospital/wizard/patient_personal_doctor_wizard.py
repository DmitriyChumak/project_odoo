from odoo import models, fields, api

class PatientPersonalDoctorWizard(models.TransientModel):
    _name = 'hr_hospital.patient.personal.doctor.wizard'
    _description = 'Patient Personal Doctor Wizard'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='New Personal Doctor', required=True)

    def action_change_personal_doctor(self):
        patients = self.env['hr_hospital.patient'].browse(self.env.context.get('active_ids'))
        for patient in patients:
            patient.personal_doctor_id = self.doctor_id
