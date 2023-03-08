# -*- coding: utf-8 -*-
{
    'name': "payasos",

    'summary': """
        Payasos a domicilio
    """,

    'description': """
        Gestion de una empresa de payasos a domicilio, con clientes y ubicaciones de fiestas.
    """,

    'author': "Daniel Gonzalez",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
       'demo/demo.xml',
    ],
}
