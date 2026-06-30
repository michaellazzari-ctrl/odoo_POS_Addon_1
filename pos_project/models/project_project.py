# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    # POS-specific fields
    pos_order_count = fields.Integer(
        string='POS Orders Count',
        compute='_compute_pos_order_count',
        store=False
    )

    @api.depends('name')
    def _compute_pos_order_count(self):
        """Compute the number of POS orders for this project"""
        for project in self:
            project.pos_order_count = 0
