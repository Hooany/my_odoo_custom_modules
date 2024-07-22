# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# controller para renderizar la página web
class WebsiteCustomController(http.Controller):
    @http.route('/cuestionario', type='http', auth='public', website=True)
    def custom_page_show(self, **kwargs):
        partner_id = kwargs.get('partner_id', '0')
        print("partner ID a enviar:", partner_id)
        return request.render('basic_web_test.custom_page_template',{'partner_id': partner_id }) #le paso el nombre del modulo basic_web_test y el nombre del template de mi web (el id)


#     # controller del botón de submit para agregar las respuestas a la db con el correspondiente ID de res.partner
class ButtonCustomController(http.Controller):
    @http.route('/cuestionario/button_action', type='http', auth='public', website=True)
    def create_records(self, **kwargs):
        print("datos recibidos: ", kwargs)
        # creo un nuevo diccionario con los valores de nombres key correctos
        correct_mapping = {
            'partner_id': 'id',
            'name': 'name',
            'pregunta1': 'pregunta1',
            'pregunta2': 'pregunta2',
            'pregunta3': 'pregunta3'
        }

        # creo otro diccionario que será el que use para updatear la db
        transformed_data = {}
        # traspaso los valores correspondientes
        for key, value in kwargs.items():
            new_key = correct_mapping.get(key, key)
            transformed_data[new_key] = value
        print("datos transformados:",transformed_data)

        # actualizo db
        partner_id = transformed_data.get('id')
        if not partner_id:
            return request.render('website_custom_module.error_template', {'error': 'Partner ID is missing'})

        # Search for the existing record
        record = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)

        if record:
            # Update the existing record with the transformed data
            record.sudo().write(transformed_data)
            message = "Record updated successfully"
        else:
            # Handle the case where the record is not found
            message = "Record not found"

        # For demonstration, redirect to a confirmation page
        return request.render('basic_web_test.pagina_gracias', {'message': message})

        # request.env['res.partner'].sudo().write(transformed_data)

        # return request.render('basic_web_test.pagina_gracias',{})
