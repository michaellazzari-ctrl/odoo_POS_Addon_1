from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    project_id = fields.Many2one(
        "project.project",
        string="Project",
        index=True,
    )

    project_name = fields.Char()

    @api.model
    def _order_fields(self, ui_order):
        values = super()._order_fields(ui_order)

        values["project_id"] = ui_order.get("project_id")
        values["project_name"] = ui_order.get("project_name")

        return values
