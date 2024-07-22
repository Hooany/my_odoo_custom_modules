# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomButtonCuestionario(models.Model):
    _inherit = 'res.partner'

    def custom_boton_cuestionario(self):

        base_url = 'http://localhost:8069/cuestionario'

        url = f"{base_url}?id={self.id}&name={self.name}"
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'new',
        }