/** @odoo-module **/

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {

    setup() {
        super.setup(...arguments);

        this.project_id = this.project_id || null;
        this.project_name = this.project_name || "";
    },

    setProject(project) {
        if (!project) {
            this.project_id = null;
            this.project_name = "";
            return;
        }

        this.project_id = project.id;
        this.project_name = project.name;
    },

    getProjectId() {
        return this.project_id;
    },

    getProjectName() {
        return this.project_name;
    },

    export_as_JSON() {
        const json = super.export_as_JSON();

        json.project_id = this.project_id;
        json.project_name = this.project_name;

        return json;
    },

    init_from_JSON(json) {
        super.init_from_JSON(...arguments);

        this.project_id = json.project_id || null;
        this.project_name = json.project_name || "";
    },

    export_for_printing() {
        const receipt = super.export_for_printing();

        receipt.project_name = this.project_name;

        return receipt;
    },

});
