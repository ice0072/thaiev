# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    is_payment_with_credit_note = fields.Boolean(
        string="Is a payment with credit note",
    )
    credit_note_reference = fields.Many2one(
        comodel_name="account.move",
        string="Credit Note Reference",
        domain="[('move_type', '=', 'out_refund'), ('state', '=', 'posted')]",
    )

    @api.depends("journal_id", "partner_id", "partner_type", "is_internal_transfer")
    def _compute_destination_account_id(self):
        res = super(AccountPayment, self)._compute_destination_account_id()
        for pay in self:
            if pay.is_internal_transfer:
                pay.destination_account_id = pay.journal_id.suspense_account_id
        return res
