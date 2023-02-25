# -*- coding: utf-8 -*-
{
    'name': "Taberna",

    'summary': """
        Gestor de taberna medieval.""",

    'description': """
        Gestor de taberna medieval que permite el control de los datos de la taberna, 
        sus empleados, bebidas disponibles, clientes y los pedidos realizados.
    """,

    'author': "Javier Marín Hernández",
    'website': "https://acortar.link/kxKBoP",

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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
