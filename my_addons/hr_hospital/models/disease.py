from odoo import models, fields

class Disease(models.Model):
    _name = 'hr_hospital.disease'
    _description = 'Disease'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code')
    description = fields.Text(string='Description')
    parent_id = fields.Many2one('hr_hospital.disease', string='Parent Disease', index=True, ondelete='cascade')
    child_ids = fields.One2many('hr_hospital.disease', 'parent_id', string='Child Diseases')

    parent_path = fields.Char(index=True, unaccent=False)
