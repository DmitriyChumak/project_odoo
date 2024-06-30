# doctor model

from odoo import models, fields
from . import person

class Doctor(models.Model):
    _name = 'hr_hospital.doctor'
    _inherit = 'hr_hospital.person'
    _description = 'Doctor'

    specialization = fields.Char(string='Specialization')

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.last_name} {rec.first_name}"
            result.append((rec.id, name))
        return result

