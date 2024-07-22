# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CamposCuestionario(models.Model):
    _inherit = 'res.partner'

    pregunta1 = fields.Text(string='Pregunta1')
    pregunta2 = fields.Text(string='Pregunta2')
    pregunta3 = fields.Text(string='Pregunta3')
    pregunta4 = fields.Text(string='Pregunta4')
    pregunta5 = fields.Text(string='Pregunta5')
    pregunta6 = fields.Text(string='Pregunta6')
    pregunta7 = fields.Text(string='Pregunta7')
    pregunta8 = fields.Text(string='Pregunta8')
    pregunta9 = fields.Text(string='Pregunta9')
    pregunta10 = fields.Text(string='Pregunta10')
#     _description = 'custom_fields_test.custom_fields_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
