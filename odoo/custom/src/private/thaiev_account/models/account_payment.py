# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.depends("journal_id", "partner_id", "partner_type", "is_internal_transfer")
    def _compute_destination_account_id(self):
        res = super(AccountPayment, self)._compute_destination_account_id()
        for pay in self:
            if pay.is_internal_transfer:
                pay.destination_account_id = pay.journal_id.suspense_account_id
        return res
