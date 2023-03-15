# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import _, models


class TrialBalanceXslx(models.AbstractModel):
    _inherit = "report.a_f_r.report_trial_balance_xlsx"

    def _generate_report_content(self, workbook, report, data, report_data):
        res = super()._generate_report_content(workbook, report, data, report_data)
        res_data = self.env[
            "report.account_financial_report.trial_balance"
        ]._get_report_values(report, data)
        trial_balance = res_data["trial_balance"]
        total_initial_balance = (
            total_debit
        ) = total_credit = total_balance = total_ending_balance = 0.0
        for line in trial_balance:
            total_initial_balance += line["initial_balance"]
            total_debit += line["debit"]
            total_credit += line["credit"]
            total_balance += line["balance"]
            total_ending_balance += line["ending_balance"]
        report_data["sheet"].merge_range(
            report_data["row_pos"],
            0,
            report_data["row_pos"],
            1,
            _("Total"),
            report_data["formats"]["format_header_center"],
        )
        i = 2
        for total in [
            total_initial_balance,
            total_debit,
            total_credit,
            total_balance,
            total_ending_balance,
        ]:
            report_data["sheet"].write_number(
                report_data["row_pos"],
                i,
                total,
                report_data["formats"]["format_header_amount"],
            )
            i += 1
        report_data["row_pos"] += 1
        return res
