# person model

from odoo import models, fields

class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'

    id = fields.Integer(string='Person ID', required=True)
    name = fields.Char(string="Name", required=True)
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    birthdate = fields.Date(string='Birthdate')
    phone = fields.Char(string='Phone')
    photo = fields.Binary(string='Photo')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')

