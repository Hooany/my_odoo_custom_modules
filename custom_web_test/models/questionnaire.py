# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Questionnaire(models.Model):
    _name = 'custom.questionnaire'
    _description = 'Questionnaire'

    name = fields.Char(string='Name', required=True)
    link = fields.Char(string='Link', readonly=True)

    def generate_link(self):
        for record in self:
            record.link = self.env['ir.config_parameter'].get_param('web.base.url') + '/cuestionario_web/%s' % record.id