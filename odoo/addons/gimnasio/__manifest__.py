# -*- coding: utf-8 -*-
{
    'name': "Gimnasio",

    'summary': """
        Podrás gestionar tu gimansio desde este fantástico módulo""",

    'description': """
        Módulo para gestionar tu propio gimnasio
    """,

    'author': "Alberto Ruiz",
    'website': "https://strongmantarrako.net/content/7-club",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Deportes',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True
}
