# -*- coding: utf-8 -*-

from odoo import api, models, fields


class RepairOrderLine(models.Model):
    _name = 'taller.repair.order.line'

    order_id = fields.Many2one(comodel_name="taller.repair.order", required=True, ondelete="cascade", index=True, copy=False)
    qty = fields.Float(string="Quantity")
    product_id = fields.Many2one(comodel_name="product.product", string="Product")

    price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)

    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', store=True)

    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id, required=True)

    @api.depends('qty', 'price_unit')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * line.qty
            line.price_subtotal = price