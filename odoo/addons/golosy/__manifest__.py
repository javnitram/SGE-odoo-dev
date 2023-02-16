# -*- coding: utf-8 -*-
{
    'name': "Golosy",

    'summary': "Gestion de una tienda de golosinas",

    'description': "Este modulo consiste en gestionar cualquier parametro de una tienda, desde el conteo del stock, los nombres de los productos, hasta los informes para solicitar un nuevo pedido",

    'author': "Wilton SL.",
    'website': "http://www.wilton-company.com",

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
