# -*- coding: utf-8 -*-

from odoo import models, fields


class Provinces(models.Model):
    _name = 'votantes.provinces'
    _description = 'votantes.provinces'

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    description = fields.Char(string="Description")
    population = fields.Char(string="Population")

