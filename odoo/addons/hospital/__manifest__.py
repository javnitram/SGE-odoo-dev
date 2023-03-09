# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': """Gestión de un Hospital""",

    'description': """
        Gestiona la parte administrativa de un hospital de forma sencilla.
    """,

    'author': "Gilzan",
    'website': "http://www.hospitalaesperanza.com",
    
    'category': 'SGE23',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_actions.xml',
        'views/templates.xml',
        'views/views_pacientes.xml',
        'views/views_doctores.xml',
        'views/views_enfermeros.xml',
        'views/views_medicinas.xml',
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
