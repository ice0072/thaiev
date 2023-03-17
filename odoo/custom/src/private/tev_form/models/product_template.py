import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    condition= fields.Text(
        string="เงื่อนไข",
    )
    