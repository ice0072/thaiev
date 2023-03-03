from odoo import fields, models
from odoo.tools.translate import _


class AccountMoveReversal(models.TransientModel):
    """
    Account move reversal wizard, it cancel an account move by reversing it.
    """

    _inherit = "account.move.reversal"

    def _prepare_default_reversal(self, move):
        super(AccountMoveReversal, self)._prepare_default_reversal(move)
        reverse_date = self.date if self.date_mode == "custom" else move.date
        return {
            "ref": _("Reversal of: %(move_name)s", move_name=move.name),
            "date": reverse_date,
            "invoice_date": move.is_invoice(include_receipts=True)
            and (self.date or move.date)
            or False,
            "journal_id": self.journal_id and self.journal_id.id or move.journal_id.id,
            "invoice_payment_term_id": None,
            "invoice_user_id": move.invoice_user_id.id,
            "auto_post": True
            if reverse_date > fields.Date.context_today(self)
            else False,
            "reason": self.reason,
        }
