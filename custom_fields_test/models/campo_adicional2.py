# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CampoAdicional2(models.Model):
    _inherit = 'res.partner'

    custom_field_2 = fields.Text(string='Custom Field')
