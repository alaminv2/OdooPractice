from odoo import api, fields, models
import datetime

class doctorS(models.Model):
    _name = 'doctor.doctor'
    _rec_name = 'doctor_name'
    _description = 'Doctor Description'

    name = fields.Char(string="Doctor ID", readonly=True, index=True, copy=False, default=lambda s: 'New')
    doctor_name = fields.Char(string="Doctor Name", required=True)
    doctor_age = fields.Integer(string="Age")
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender",default='male')
    # related_user = fields.Many2one('res.users', string='Related User')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New' == 'New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('doctor.sequence') or "New"
        res = super(doctorS, self).create(vals)
        return res

