# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"
    _state_from = ["to_approve"]
    _state_to = ["approved"]
    _cancel_state = "rejected"

    def button_to_approve(self):
        res = super().button_to_approve()
        # Request Validation
        for request in self:
            request.request_validation()
        return res
