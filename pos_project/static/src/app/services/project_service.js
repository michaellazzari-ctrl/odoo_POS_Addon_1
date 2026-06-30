/** @odoo-module **/

import { registry } from "@web/core/registry";

export const ProjectService = {
    start(env) {

        function getProjectsForPartner(partner) {

            if (!partner || !partner.x_ADR_ID) {
                return [];
            }

            return env.pos.models["project.project"].filter(
                project => project.x_partner_id === partner.x_ADR_ID
            );

        }

        return {
            getProjectsForPartner,
        };
    },
};

registry.category("services").add("project_service", ProjectService);
