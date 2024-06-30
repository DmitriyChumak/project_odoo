# patient model

from odoo import models, fields, api
from datetime import *
from . import person


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _inherit = 'hr_hospital.person'
    _description = 'Patient'

    personal_doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal Doctor')
    passport_data = fields.Char(string='Passport Data')
    contact_person = fields.Char(string='Contact Person')

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.last_name} {rec.first_name}"
            result.append((rec.id, name))
        return result

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year - (
                            (today.month, today.day) < (rec.date_of_birth.month, rec.date_of_birth.day))
            else:
                rec.age = 0

    age = fields.Integer(string='Age', compute='_compute_age', store=True)