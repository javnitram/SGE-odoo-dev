# -*- coding: utf-8 -*-
{
    'name': "armas",

    'summary': """
        Esta se trata de una tienda family friendly para los amantes de las armas""",

    'description': """
        Este módulo consiste en un historial de armas vendidas en una tienda a clientes

    """,

    'author': "Adrian CD",
    'website': "https://www.rangertienda.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Armamento',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
