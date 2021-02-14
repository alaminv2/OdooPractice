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
    ], string="Gender", default='male')
    dob = fields.Datetime(string="Birth Date", default=datetime.datetime.now())
    appointment_count = fields.Integer(compute="get_number_of_appointments", default=0)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New' == 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('patient.sequence') or "New"
        res = super(patientS, self).create(vals)
        return res

    # For Appointments smart button
    def patients_appointments(self):
        print('In patients_appointments func...')
        return {
            'name': 'Appointments',
            'type': 'ir.actions.act_window',
            'res_model': 'appointment.appointment',
            'view_mode': 'tree,form',
            'domain': '[("patient_id", "=", self.id)]',
            'view_id': False,
            # 'name': 'Appointments',
            # 'res_model': 'hospital.appoinment',
            # 'view_mode': 'tree,form',
            # 'domain': [('patient_id', '=', self.id)],
            # 'type': 'ir.actions.act_window',
            # 'view_id': False,
        }

    def get_number_of_appointments(self):
        self.appointment_count = self.env['appointment.appointment'].search_count([('patient_id', '=', rec.id)])
        print('num of appointments = ', self.appointment_count)
