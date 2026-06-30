from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    pos_order_ids = fields.One2many(
        comodel_name="pos.order",
        inverse_name="project_id",
        string="POS Orders",
    )

    pos_order_count = fields.Integer(
        string="POS Orders",
        compute="_compute_pos_statistics",
        store=False,
    )

    pos_amount_total = fields.Monetary(
        string="POS Sales",
        compute="_compute_pos_statistics",
        currency_field="company_currency_id",
        store=False,
    )

    company_currency_id = fields.Many2one(
        related="company_id.currency_id",
        readonly=True,
    )

    @api.depends("pos_order_ids.amount_total")
    def _compute_pos_statistics(self):
        for project in self:
            project.pos_order_count = len(project.pos_order_ids)
            project.pos_amount_total = sum(project.pos_order_ids.mapped("amount_total"))
