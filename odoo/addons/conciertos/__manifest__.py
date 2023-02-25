# -*- coding: utf-8 -*-
{
    'name': 'Conciertos',

    'summary': """
        Módulo de gestión de conciertos, artistas, recintos y venta de entradas""",

    'description': """
        Long description of module's purpose
    """,

    'author': 'Samuel Amaro',
    'website': 'https://amsamu.github.io',

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
        'views/views_artista.xml',
        'views/views_cliente.xml',
        'views/views_concierto.xml',
        'views/views_entrada.xml',
        'views/views_recinto.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
