# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.model
    def _get_under_validation_exceptions(self):
        res = super()._get_under_validation_exceptions()
        res.extend(["tax_invoice_ids", "wht_move_ids", "to_clear_tax"])
        return res
