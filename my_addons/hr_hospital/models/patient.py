# patient model

from odoo import models, fields
from . import person

class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _inherit = 'hr_hospital.person'
    _description = 'Patient'

    def name_get(self):
        result = []
        for rec in self:
            name = f"{rec.last_name} {rec.first_name}"
            result.append((rec.id, name))
        return result

