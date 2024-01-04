# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _name = 'taller.car'
    _description = 'taller.car'

    #Cargando un campo del modelo de Contactos
    customer_id = fields.Many2one("res.partner", string="Customer", required=True)
    #Cargando un campo del Contacto
    country_id = fields.Many2one(string="Customer Country", related="customer_id.country_id", readonly=True)

    name = fields.Char(string="Model", default="New")
    registration = fields.Char(string="Registration", required=True, help="Ingrese matricula del vehículo")
    brand = fields.Many2one(comodel_name="taller.brand", string="Brand")
    date_car = fields.Date("Date Car", required=True)
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
