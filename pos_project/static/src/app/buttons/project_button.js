/** @odoo-module **/

import { Component } from "@odoo/owl";

export class ProjectButton extends Component {

    static template = "pos_project.ProjectButton";

    get currentOrder() {
        return this.env.pos.get_order();
    }

    get partner() {
        return this.currentOrder.get_partner();
    }

}
