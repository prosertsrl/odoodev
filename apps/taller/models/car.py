# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = 'taller.car'
    _description = 'taller.car'

    name = fields.Char(string="Name")
    registration = fields.Char(string="Registration")
    brand = fields.Char(string="Brand")
    date_car = fields.Date("Date Car")
    km = fields.Integer("Km")
    cylinder = fields.Integer(string="Cylinder")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
