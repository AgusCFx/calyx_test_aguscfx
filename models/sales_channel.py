from odoo import models, fields, api
import logging


class SalesChannel(models.Model):
    _name = "sales.channel"
    _inherit = "mail.thread"
    _description = "Canal de Venta"

    name = fields.Char(string="Nombre", required=True, tracking=True)
    codigo = fields.Char(string="Codigo",readonly=True, copy=False, default="Nuevo")
    #TODO cambiar sufijos de many2one a _id
    deposito = fields.Many2one(comodel_name='stock.warehouse')
    diario_de_factura = fields.Many2one(comodel_name='account.journal')

    # Agrega secuencia +1 a campo 'codigo' al crear nuevo registro
    @api.model
    def create(self, vals):
        if vals.get('codigo', 'Nuevo') == 'Nuevo':
            vals['codigo'] = self.env['ir.sequence'].next_by_code('sales.channel.code.secuence') or 'Nuevo'
        return super(SalesChannel, self).create(vals)

    