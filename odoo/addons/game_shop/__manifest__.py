# -*- coding: utf-8 -*-
{
    'name': "game_shop",

    'summary': """
        Módulo que nos permitirá gestionar tiendas de videojuegos""",

    'description': """
        En este módulo lo que podremos hacer es:
        -Dar de alta/baja nuevas tiendas
        -Dar de alta/baja nuevos juegos
        -Añadir videojuegos a las tiendas donde se quiere vender
        -Cada tienda podrá referenciar donde se encuentra su almacen
        
        En resumen nos permite gestionar una tienda de videojuegos
    """,

    'author': "Santiago Bricio Rojas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

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
