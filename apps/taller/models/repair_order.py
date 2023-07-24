# -*- coding: utf-8 -*-

from odoo import models, fields


class RepairOrder(models.Model):
    _name = 'taller.repair.order'
    _description = 'taller.repair'

    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer", required=True)

    name = fields.Char(string="Name", default="New")
    date = fields.Date(string="Date Order")

    line_ids = fields.One2many(comodel_name="taller.repair.order.line", inverse_name="order_id")



