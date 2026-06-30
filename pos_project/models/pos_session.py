# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()

        result.append("project.project")

        return result

    def _loader_params_project_project(self):
        return {
            "search_params": {
                "fields": [
                    "id",
                    "name",
                    "x_partner_id",
                ],
            },
        }

    def _get_pos_ui_project_project(self, params):
        return self.env["project.project"].search_read(**params["search_params"])
