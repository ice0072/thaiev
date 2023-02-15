# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    payment_info_name = fields.Char(compute="_compute_payment_info_name")

    def _compute_payment_info_name(self):
        """
        This function returns name of the payment info.\n
        After register payment.
        """
        reconciles = self._get_reconciled_info_JSON_values()
        payment = []
        for rec in reconciles:
            payment.append(rec["ref"].split()[0])
        self.payment_info_name = " ".join(payment)
