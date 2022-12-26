# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


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
        return super()._approval_allowed()
