# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class QuestionnaireController(http.Controller):

    @http.route('/cuestionario_web', type='http', auth='public', website=True)
    # def questionnaire_form(self, questionnaire_id, **kwargs):
    def question_client(self, **kwargs):
        return http.request.render('custom_web_test.questionnaire_form')
        # questionnaire = request.env['custom.questionnaire'].sudo().browse(questionnaire_id)
        # return request.render('custom_questionnaire.questionnaire_form', {'questionnaire': questionnaire})


    @http.route('/questionnaire/submit', type='http', auth='public', website=True)
    def questionnaire_submit(self):
        #
        #     request.env['custom.questionnaire.submission'].sudo().create({
        #         'questionnaire_id': post.get('questionnaire_id'),
        #         'response': post.get('response'),
        #     })
        return http.request.render('custom_questionnaire.thank_you')
