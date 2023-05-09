import logging
import re

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def get_invoices(self):
        invoices=self.ref.split(' ')
        invoice_data=self.env['account.move'].search([('name','in',invoices)])
        return invoice_data