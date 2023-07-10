# -*- coding: utf-8 -*-

from odoo import models, fields


class Brand(models.Model):
    _name = 'taller.brand'
    _description = 'taller.brand'

    name = fields.Char(string="Name", default="New")
    image = fields.Binary(string="Image")