import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

class mydemo(models.Model):
    _name = 'my.demo'
    _description = 'mydemo'

    name = fields.Char()
    active = fields.Boolean(default=True)
    
