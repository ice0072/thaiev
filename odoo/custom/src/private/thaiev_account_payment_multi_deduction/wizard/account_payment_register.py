# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    writeoff_analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Analytic Account",
        index=True,
    )
    writeoff_analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        string="Analytic Tags",
    )
    deduct_analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        compute="_compute_default_analytic",
    )
    deduct_analytic_tag_ids = fields.Many2many(
        comodel_name="account.analytic.tag",
        compute="_compute_default_analytic",
    )

    @api.depends("payment_difference", "deduction_ids")
    def _compute_default_analytic(self):
        active_ids = self.env.context.get("active_ids")
        moves = self.env["account.move"].browse(active_ids)
        move_lines = moves.mapped("line_ids")
        analytic_account = move_lines.mapped("analytic_account_id")
        analytic_tag = move_lines.mapped("analytic_tag_ids")
        taxes_account = (
            self.env["account.tax.repartition.line"]
            .search([("account_id", "!=", False)])
            .mapped("account_id")
        )
        moves_without_tax = move_lines.filtered(
            lambda l: l.account_id.user_type_id.type not in ("payable", "receivable")
            and l.account_id.id not in taxes_account.ids
        )
        default_tag = (
            all(line.analytic_tag_ids == analytic_tag for line in moves_without_tax)
            and analytic_tag
            or False
        )
        for rec in self:
            rec.deduct_analytic_account_id = (
                len(analytic_account) == 1 and analytic_account.id or False
            )
            rec.deduct_analytic_tag_ids = default_tag

    def _update_vals_deduction(self, moves):
        move_lines = moves.mapped("line_ids")
        analytic_account = move_lines.mapped("analytic_account_id")
        analytic_tag = move_lines.mapped("analytic_tag_ids")
        taxes_account = (
            self.env["account.tax.repartition.line"]
            .search([("account_id", "!=", False)])
            .mapped("account_id")
        )
        moves_without_tax = move_lines.filtered(
            lambda l: l.account_id.user_type_id.type not in ("payable", "receivable")
            and l.account_id.id not in taxes_account.ids
        )
        default_tag = (
            all(line.analytic_tag_ids == analytic_tag for line in moves_without_tax)
            and analytic_tag
            or False
        )
        self.writeoff_analytic_account_id = (
            len(analytic_account) == 1 and analytic_account.id or False
        )
        self.writeoff_analytic_tag_ids = default_tag

    @api.onchange("payment_difference", "payment_difference_handling")
    def _onchange_default_deduction(self):
        if self.payment_difference_handling == "reconcile":
            active_ids = self.env.context.get("active_ids", [])
            moves = self.env["account.move"].browse(active_ids)
            self._update_vals_deduction(moves)
