# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

# extending Model we create business objects
class EstateProperty(models.Model):
    _name = 'estate_property' #name is required and defines the name of the new model
# a new database table will be created, named test_model
    _description = 'Estate property'

# Calculate the date 3 months from today
    @api.model
    def _default_date_availability(self):
        return date.today() + relativedelta(months=3)

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postal code')
    date_availability = fields.Date(
        string='Date availability',
        copy=False,
        default=_default_date_availability)
    expected_price = fields.Float(string='Expected price', required=True)
    selling_price = fields.Float(string='Selling price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_area = fields.Integer(string='Living area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden area')
    garden_orientation = fields.Selection(
        string='Garden orientation',
        selection=[('north','North'),
                   ('south','South'),
                   ('west','West'),
                   ('east','East')],
        help='Determines the garden orientation')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(
        string='State',
        selection=[('new','New'),
                   ('offer_received','Offer received'),
                   ('offer_accepted','Offer accepted'),
                   ('sold','Sold'),
                   ('canceled','Canceled')],
        help='Property state',
        required=True,
        copy=False,
        default='new')
