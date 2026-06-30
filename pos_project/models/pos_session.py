
from odoo import models, fields, api


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_res_partner(self):
    params = super()._loader_params_res_partner()

    params["search_params"]["fields"].append("x_ADR_ID")

    return params

