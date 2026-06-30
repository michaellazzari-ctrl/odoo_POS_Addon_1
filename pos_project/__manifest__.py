{
    "name": "POS Project",
    "version": "19.0.1.0.0",
    "author": "Michael Lazzari",
    "website": "https://github.com/michaellazzari-ctrl",
    "license": "LGPL-3",
    "category": "Point of Sale",
    "summary": "Link POS orders to Projects",
    "depends": [
        "point_of_sale",
        "project",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/pos_order_views.xml",
        "views/pos_config_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_project/static/src/js/**/*.js",
            "pos_project/static/src/xml/**/*.xml",
            "pos_project/static/src/scss/**/*.scss",
        ],
    },
    "installable": True,
    "application": False,
}
