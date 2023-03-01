# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    amount_currency = fields.Float(
        compute="_compute_amount_currency",
    )

    def _compute_amount_currency(self):
        for rec in self:
            amount = rec.currency_id._convert(
                rec.amount, rec.company_id.currency_id, rec.company_id, rec.date
            )
            rec.amount_currency = amount
