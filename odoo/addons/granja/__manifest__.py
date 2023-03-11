# -*- coding: utf-8 -*-
{
    # Descripcion del modulo
    'name': "Granja",

    'summary': """
        Modulo para la gestión de una granja
    """,

    'description': """
        Modulo para la gestión de una granja
    """,

    'author': "Ricardo Hernandez Lopez",
    'website': "http://www.ricardohl.com",

    'category': 'SGE24',
    'version': '0.1',

    'depends': ['base'],

    # Archivos de datos
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    # Datos de demo
    'demo': [
        'demo/demo.xml',
    ],
}
