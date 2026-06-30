# -*- coding: utf-8 -*-
{
    'name': 'POS Project Addon',
    'version': '1.0.0',
    'category': 'Point of Sale',
    'summary': 'Point of Sale Addon for enhanced functionality',
    'author': 'Your Name',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_order_views.xml',
        'views/pos_config_views.xml',
    ],
    'installable': True,
    'application': False,
}
