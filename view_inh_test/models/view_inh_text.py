# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ViewInhTest(models.Model):
    _inherit = 'res.partner'

    custom_field_3 = fields.Text(string='Custom Field')
