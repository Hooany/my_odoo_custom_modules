# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CampoAdicional1(models.Model):
    _inherit = 'res.partner'

    custom_field_1 = fields.Text(string='Custom Field')
