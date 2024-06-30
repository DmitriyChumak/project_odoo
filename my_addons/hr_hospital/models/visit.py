# visit model

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from . import person

class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    state = fields.Selection([
        ('planned', 'Planned'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='planned')
    planned_date_time = fields.Datetime(string='Planned Date & Time')
    actual_date_time = fields.Datetime(string='Actual Date & Time')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor', required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient', required=True)
    diagnosis_ids = fields.One2many('hr_hospital.diagnosis', 'visit_id', string='Diagnoses')
    symptoms = fields.Text(string='Symptoms')
    notes = fields.Text(string='Notes')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'completed':
            self.actual_date_time = fields.Datetime.now()
            # Заборона на зміну даних після завершення візиту
            self.planned_date_time = self.actual_date_time
            self.doctor_id = self.doctor_id

    @api.constrains('patient_id', 'doctor_id', 'date')
    def _check_unique_patient_doctor_date(self):
        for rec in self:
            if rec.search_count([
                ('patient_id', '=', rec.patient_id.id),
                ('doctor_id', '=', rec.doctor_id.id),
                ('date', '>=', rec.date.date()),
                ('date', '<', rec.date.date() + timedelta(days=1)),
                ('id', '!=', rec.id),
            ]):
                raise ValidationError("This patient already has a visit scheduled with this doctor on this date.")

    @api.ondelete(at_uninstall=False)
    def _unlink_except_with_diagnosis(self):
        for visit in self:
            if visit.diagnosis_ids:
                raise UserError(_(
                    "You cannot delete a visit that has diagnoses associated with it."
                ))