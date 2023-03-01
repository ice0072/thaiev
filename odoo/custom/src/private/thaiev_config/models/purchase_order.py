# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    amount_total_currency = fields.Float(
        compute="_compute_amount_total_currency",
    )

    def _compute_amount_total_currency(self):
        for rec in self:
            amount = rec.currency_id._convert(
                rec.amount_total,
                rec.company_id.currency_id,
                rec.company_id,
                rec.create_date.date(),
            )
            rec.amount_total_currency = amount
