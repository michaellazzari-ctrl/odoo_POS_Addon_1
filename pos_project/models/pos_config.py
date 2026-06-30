# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    # Add custom configuration fields here
    custom_config = fields.Boolean(string='Custom Configuration', default=False)
    config_parameter = fields.Char(string='Configuration Parameter')
