import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"

    autograph=fields.Binary(
        string="ลายเซ็น",
        attachment=True
    )
    
    def __init__(self, pool, cr):
        """Override of __init__ to add access rights.
        Access rights are disabled by default, but allowed
        on some specific fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """

        tev_form_writeable_fields = [
            "autograph",
        ]

        init_res = super().__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = (
            type(self).SELF_READABLE_FIELDS + tev_form_writeable_fields
        )
        type(self).SELF_WRITEABLE_FIELDS = (
            type(self).SELF_WRITEABLE_FIELDS + tev_form_writeable_fields
        )
        return init_res
