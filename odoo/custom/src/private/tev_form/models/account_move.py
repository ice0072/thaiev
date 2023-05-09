import logging
import re

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    @staticmethod
    # ดึงชื่ออันเก่า
    def old_invoice(ref):
        regex_str = r"INV\/\d{4}\/\d{2}\/\d{4}"

        match = re.search(regex_str, ref)
        if match:
            output_str = match.group(0)
            return output_str
        else:
            return False
    

    def old_amount_total_invoice(self):
        old_invoice_data=self.env['account.move'].search([('name','=',self.old_invoice(self.ref))])
        return old_invoice_data[0].amount_untaxed
    
    def correct_value(self):
        old_invoice_data=self.env['account.move'].search([('name','=',self.old_invoice(self.ref))])
        return old_invoice_data[0].amount_untaxed - self.amount_untaxed
    
    def old_invoice_date(self):
        old_invoice_data=self.env['account.move'].search([('name','=',self.old_invoice(self.ref))])
        if len(old_invoice_data) > 0:
            return old_invoice_data[0].invoice_date
        return False
    
    def old_invoice_name(self):
        old_invoice_data=self.env['account.move'].search([('name','=',self.old_invoice(self.ref))])
        return old_invoice_data[0].name

    def payment_name(self):
        accont_payment_data=self.env['account.payment'].search([('ref','ilike',f'%{self.name}%')])
        if(len(accont_payment_data)>0):
            return accont_payment_data[0].name
        return ""

    def payment_date(self):
        accont_payment_data=self.env['account.payment'].search([('ref','ilike',f'%{self.name}%')])
        if(len(accont_payment_data)>0):
            return accont_payment_data[0].date
        return ""

