# person model

from odoo import models, fields

class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'

    last_name = fields.Char(string='Last Name')
    first_name = fields.Char(string='First Name')
    phone = fields.Char(string='Phone')
    photo = fields.Image(string='Photo')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    date_of_birth = fields.Date(string='Date of Birth')
    address = fields.Text(string='Address')
    email = fields.Char(string='Email')

