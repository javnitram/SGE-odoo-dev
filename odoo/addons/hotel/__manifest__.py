# -*- coding: utf-8 -*-
{
    'name': "hotel",

    'summary': """
        Reserva de habitación de hotel para clientes
    """,

    'description': """
        Módulo que sirve para resrvar habitaciones de hotel para los clientes
    """,

    'author': "Juan Fernández Hinojar",
    'website': "http://www.trivago.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SGE23',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/reservaView.xml',
        'views/clienteView.xml',
        'views/habitacionView.xml',
        'views/empresaView.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True
}
