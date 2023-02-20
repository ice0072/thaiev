# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _state_from = ["to approve"]
    _state_to = ["purchase"]
    _cancel_state = "cancel"

    def button_confirm(self):
        res = super().button_confirm()
        for order in self:
            if order.state == "to approve":
                order.request_validation()
        return res

    def _approval_allowed(self):
        if self._context.get("bypass_check_approval_allowed", False):
            return True
        # Overwrite core function
        return self.company_id.po_double_validation == "one_step" or (
            self.company_id.po_double_validation == "two_step"
            and self.amount_total
            < self.env.company.currency_id._convert(
                self.company_id.po_double_validation_amount,
                self.currency_id,
                self.company_id,
                self.date_order or fields.Date.today(),
            )
        )
