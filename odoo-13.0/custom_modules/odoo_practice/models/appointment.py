from odoo import api, fields, models
import datetime

class appointmenT(models.Model):
    _name = 'appointment.appointment'
    _rec_name = 'patient_id'
    _description = 'Doctor Description'

    name = fields.Char(string="Doctor ID", readonly=True, index=True, copy=False, default=lambda s: 'New')
    patient_id = fields.Many2one('patient.patient', string="Patient", required=True)
    date = fields.Datetime(string='Date', default=datetime.datetime.now())
    doctor_ids = fields.Many2many('doctor.doctor', 'appointment_doctor_rel', string='Doctors')


    @api.model
    def create(self, vals):
        if vals.get('name', 'New' == 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or "New"
        res = super(appointmenT, self).create(vals)
        return res

