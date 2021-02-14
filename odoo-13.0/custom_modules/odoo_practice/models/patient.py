from odoo import api, fields, models
import datetime

class patientS(models.Model):
    _name = 'patient.patient'
    _rec_name = 'patient_name'
    _description = 'Patient Description'

    name = fields.Char(string="Patient ID", readonly=True, index=True, copy=False, default=lambda s: 'New')
    patient_name = fields.Char(string="Patient Name", required=True)
    patient_age = fields.Integer(string="Age")
    patient_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender",default='male')
    dob = fields.Datetime(string="Birth Date", default=datetime.datetime.now())

    @api.model
    def create(self, vals):
        if vals.get('name', 'New' == 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.sequence') or "New"
        res = super(patientS, self).create(vals)
        return res

