# -*- coding: utf-8 -*-

from odoo import models, fields


class taller(models.Model):
    _name = 'taller.car'
    _description = 'taller.car'

    name = fields.Char(string="Name")
    tuition = fields.Char(string="Tuition")
    brand = fields.Char(string="Brand")
    date_car = fields.Date(string="Date Car")
    km = fields.Integer(string="Km")



