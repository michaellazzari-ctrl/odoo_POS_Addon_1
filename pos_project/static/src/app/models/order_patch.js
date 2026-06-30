/** @odoo-module **/

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {

    setup() {
        super.setup(...arguments);

        this.project_id = null;
        this.project_name = null;
    },

    export_as_JSON() {

        const json = super.export_as_JSON();

        json.project_id = this.project_id;
        json.project_name = this.project_name;

        return json;
    },

    init_from_JSON(json) {

        super.init_from_JSON(...arguments);

        this.project_id = json.project_id;
        this.project_name = json.project_name;
    },

});
