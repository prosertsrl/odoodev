# -*- coding: utf-8 -*-

from odoo import models, fields


class Car(models.Model):
    _inherit = 'taller.car'

    image = fields.Image(string="Image")
