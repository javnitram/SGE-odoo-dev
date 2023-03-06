# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """Gestión de un Hospital""",

    'description': """
        Gestiona la parte administrativa de un hospital de forma sencilla.
    """,

    'author': "Gilzan",
    'website': "http://www.hospitalesperanza.com",
    
    'category': 'SGE23',
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
        'demo/doctores.xml',
        'demo/pacientes.xml',
        'demo/enfermeros.xml',
        'demo/medicinas.xml',
    ],
    
    'application': True
}
