# -*- coding: utf-8 -*-
{
    'name': "reBuy",

    'summary': """
        Module oriented to second hand stores business model.""",

    'description': """
        Module for second hand stores, with buy-and-sell businesses needs in mind, containing utilities that help managing the process of selling products
        and buying from clients.
    """,

    'author': "Alicia Medina",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/client.products.view.xml',
        'views/products.view.xml',
        'views/items.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
