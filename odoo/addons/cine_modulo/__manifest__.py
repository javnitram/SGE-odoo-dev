# -*- coding: utf-8 -*-
{
    'name': "Cine_modulo",

    'summary': """
        Modulo de cine.
        """,

    'description': 
    """
       Módulo que se utiliza para seguir un registro de un cine con sus empleados, sus clientes, las peliculas disponibles y las distribuidoras
    """,

    'author': "Jaime Díaz Fenández",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'AOTY (Application Of The Year)',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

}
