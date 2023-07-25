import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"

    autograph=fields.Binary(
        string="ลายเซ็น",
        attachment=True
    )
