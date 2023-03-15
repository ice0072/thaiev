# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, models


class TrialBalanceReport(models.AbstractModel):
    _inherit = "report.account_financial_report.trial_balance"

    def _get_report_name(self):
        return _("Trial Balance")

    def _get_report_values(self, docids, data):
        res = super()._get_report_values(docids, data)
        res.update({"report_name": self._get_report_name()})
        return res
