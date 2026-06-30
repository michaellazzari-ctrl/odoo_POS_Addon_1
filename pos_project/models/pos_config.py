from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    project_required = fields.Boolean(
        string="Project Required",
        default=False,
        help="Require a project before validating the payment.",
    )
