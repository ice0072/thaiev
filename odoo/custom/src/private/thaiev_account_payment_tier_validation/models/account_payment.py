# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        context = dict(self._context)
        res = super(AccountPayment, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        if (
            res
            and view_type in ["tree", "form"]
            and context.get("default_payment_type") == "outbound"
        ):
            # Remove reports print button if its not customer
            for rec in res.get("toolbar", {}).get("print", []):
                del res["toolbar"]["print"][
                    res.get("toolbar", {}).get("print").index(rec)
                ]
        return res
