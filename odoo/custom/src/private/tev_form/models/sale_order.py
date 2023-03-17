import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    subject = fields.Char(
        string="เรื่อง",
    )


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def create(self, vals):
        if(vals.get('product_template_id')):
            product_product=self.env['product.product'].browse(vals['product_template_id'])
            sale_order=self.env['sale.order'].browse(vals['order_id'])
            # _logger.info(f"test test {sale_order.name}")
            # _logger.info(f"test test {product_product.name}")
            if(product_product and product_product.condition and sale_order):
                sale_order.write({'note': product_product.condition})
        record = super(SaleOrderLine, self).create(vals)
        return record

    @api.depends('product_id')
    @api.onchange('product_id')
    def onchange_product_id(self):
        if(self.product_id and self.product_id.condition):
            self.order_id.note = self.product_id.condition
