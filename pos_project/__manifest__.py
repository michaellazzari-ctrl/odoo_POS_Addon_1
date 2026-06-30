# -*- coding: utf-8 -*-
{
    'name': 'POS Project Addon',
    'version': '1.0.0',
    'category': 'Point of Sale',
    'summary': 'Point of Sale Addon for enhanced functionality',
    'author': 'Your Name',
    'depends': ['point_of_sale', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_order_views.xml',
        'views/pos_config_views.xml',
        'views/project_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_project/static/src/app/models/order_patch.js',
        ],
    },
    'installable': True,
    'application': False,
}
