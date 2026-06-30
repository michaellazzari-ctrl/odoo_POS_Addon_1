from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    project_id = fields.Many2one(
        "project.project",
        string="Project",
        index=True,
        ondelete="restrict",
    )
