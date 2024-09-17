from odoo import models, fields, api
from odoo.exceptions import UserError

class CreditGroup(models.Model):
    _name ="credit.group"
    _description = "Grupo de Credito"

    name = fields.Char('Nombre', required=True)
    #TODO compute
    codigo = fields.Char('Codigo', required=True)
    
    canal_venta_id = fields.Many2one(comodel_name="sales.channel")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,    default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id', readonly=True)

    credito_global = fields.Monetary(string="Credito Global", required=True)
    credito_utilizado = fields.Monetary(string="Credito Utilizado")
    credito_disponible = fields.Monetary(string="Credito Disponible")

    @api.constrains('codigo')
    def _compute_codigo(self):
        for rec in self:
            if rec.codigo == "026":
                raise UserError("El valor del campo 'Codigo' no puede ser '026'")
            if self.search_count([('codigo','=',rec.codigo),('id','!=',rec.id)]) > 0:
                raise UserError(f"El valor '{rec.codigo}' del campo 'Codigo' ya exite, intente otro valor")