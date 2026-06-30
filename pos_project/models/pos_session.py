from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    # -------------------------------------------------------------------------
    # POS UI
    # -------------------------------------------------------------------------

    def _pos_ui_models_to_load(self):
        """Load Project model into the POS."""
        result = super()._pos_ui_models_to_load()

        if "project.project" not in result:
            result.append("project.project")

        return result

    # -------------------------------------------------------------------------
    # Partners
    # -------------------------------------------------------------------------

    def _loader_params_res_partner(self):
        """Load x_ADR_ID into the POS."""
        result = super()._loader_params_res_partner()

        fields = result["search_params"]["fields"]

        if "x_ADR_ID" not in fields:
            fields.append("x_ADR_ID")

        return result

    # -------------------------------------------------------------------------
    # Projects
    # -------------------------------------------------------------------------

    def _loader_params_project_project(self):
        """Fields loaded for project.project."""
        return {
            "search_params": {
                "domain": [],
                "fields": [
                    "id",
                    "name",
                    "x_partner_id",
                    "active",
                ],
            },
        }

    def _get_pos_ui_project_project(self, params):
        """Send projects to POS."""
        return self.env["project.project"].search_read(
            **params["search_params"]
        )
