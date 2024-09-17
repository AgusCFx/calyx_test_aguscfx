from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sales_channel_id = fields.Many2one('sales.channel', string='Canal de Ventas')

    @api.onchange('sales_channel_id')
    def _set_warehouse(self):
        if self.sales_channel_id:
            self.warehouse_id = self.sales_channel_id.deposito
        else:
            self.warehouse_id = False

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super(SaleOrder, self)._create_invoices(grouped=grouped, final=final, date=date)

        for rec in self:
            if rec.sales_channel_id:
                if rec.sales_channel_id.diario_de_factura:
                    journal_id = rec.sales_channel_id.diario_de_factura
                    res.filtered(lambda inv: inv.move_type == 'out_invoice').write({'journal_id': journal_id.id})
        return res