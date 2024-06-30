# doctor model

from odoo import models, fields, api
from . import person

class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Doctor'

    specialization_id = fields.Many2one('hr_hospital.specialization', string='Specialization')
    is_intern = fields.Boolean(string='Intern', default=False)

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.last_name} {rec.first_name}"
            result.append((rec.id, name))
        return result

    mentor_id = fields.Many2one(
        'hr_hospital.doctor',
        string='Mentor',
        domain="[('is_intern', '=', False)]",
    )