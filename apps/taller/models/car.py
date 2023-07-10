# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = 'taller.car'
    _description = 'taller.car'

    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=True)

    country_id = fields.Many2one(string="Customer Country", related="customer_id.country_id")

    name = fields.Char(string="Name", default="New")
    tuition = fields.Char(string="Tuition", required=True, help="Ingrese matricula del vehiculo", size=10)
    brand = fields.Many2one(comodel_name="taller.brand", string="Brand")
    date_car = fields.Date(string="Date Car", required=True)
    km = fields.Integer(string="Km")
