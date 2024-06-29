# disease model

from odoo import models, fields

class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Disease'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
