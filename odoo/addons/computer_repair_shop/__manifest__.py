# -*- coding: utf-8 -*-
{
    'name': "Computer Repair",

    'summary': """
        Computer repair shop management""",

    'description': """
        A module to manage the repairments, computers, parts, clients and technicians
    """,

    'author': "William Santana",
    'website': "http://example.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/repairments_views.xml',
        'views/clients_views.xml',
        'views/motherboards_views.xml',
        'views/cpu_views.xml',
        'views/ram_views.xml',
        'views/gpu_views.xml',
        'views/psu_views.xml',
        'views/chassis_views.xml',
        'views/technicians_views.xml',
        'views/computers_views.xml',
        'menu/menu.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/motherboards_demodata.xml',
        'demo/ram_demodata.xml',
        'demo/gpu_demodata.xml',
        'demo/cpu_demodata.xml',
        'demo/psu_demodata.xml',
        'demo/chassis_demodata.xml',
        'demo/technicians_demodata.xml',
        'demo/clients_demodata.xml',
        'demo/computers_demodata.xml',
    ],
}
