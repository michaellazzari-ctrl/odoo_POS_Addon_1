# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    # Add custom fields here
    custom_field = fields.Char(string='Custom Field')

    @api.onchange('custom_field')
    def _onchange_custom_field(self):
        """Handle changes to custom field"""
        pass
