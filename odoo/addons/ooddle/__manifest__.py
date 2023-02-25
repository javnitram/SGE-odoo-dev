# -*- coding: utf-8 -*-
{
    'name': "Ooddle",

    'summary': """
        Model for managing a paddle club""",

    'description': """
         Model for managing a paddle club
    """,

    'author': "David Millan",
    'website': "https://github.com/Daviis00",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Paddle',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/users.views.xml',
        'views/menu.items.xml',
        'views/matches.views.xml', 
        'views/courts.views.xml',
        'views/teams.views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        
    ],
}
