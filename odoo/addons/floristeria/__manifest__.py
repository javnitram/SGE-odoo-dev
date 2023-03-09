# -*- coding: utf-8 -*-
{
    'name': "Floristeria",

    'summary': """Módulo para gestionar una floristería""",

    'description': """Este módulo incorpora funciones para poder gestionar una floristería.
        Clasificar flores según su especie. 
        Crear ramos de flores y macetas.
        Gestionar los encargados""",

    'author': "Hector Fernandez Ruiz",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
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
