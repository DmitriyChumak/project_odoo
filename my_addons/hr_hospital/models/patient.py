from odoo import models, fields, api
from . import person

class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _inherit = 'hr_hospital.person'
    _description = 'Patient'

    personal_doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal Doctor')
    supervised_doctor_id = fields.Many2one('hr_hospital.doctor', string='Supervised Doctor')
    disease_ids = fields.Many2many('hr_hospital.disease', string='Diseases')
    visit_ids = fields.One2many('hr_hospital.visit', 'patient_id', string='Visits')
    passport_info = fields.Char(string='Passport Information')
    contact_person = fields.Char(string='Contact Person')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days // 365
            else:
                record.age = 0
