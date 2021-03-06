from odoo import api, fields, models


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    @api.multi
    def _compute_quant_package_ids(self):
        for picking in self:
            picking.quant_package_ids = [packs.id for packs in picking.package_ids]

    quant_package_ids = fields.Many2many(
        compute='_compute_quant_package_ids',
        comodel_name='stock.quant.package',
        string='Physical packages',
        store=False
    )
