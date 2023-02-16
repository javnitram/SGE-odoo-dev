# -*- coding: utf-8 -*-
{
    'name': "ooddle",

    'summary': """
        Modulo para gestionar un club de padel""",

    'description': """
         Modulo para gestionar un club de padel
    """,

    'author': "David Millan",
    'website': "http://www.yourcompany.com",

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
