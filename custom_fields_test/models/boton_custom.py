# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TestCustomButton(models.Model):
    _inherit = 'res.partner'

    def custom_button_method(self):
        print("boton presionado")
