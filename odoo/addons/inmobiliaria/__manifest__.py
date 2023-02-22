# -*- coding: utf-8 -*-
{
    'name': "inmobiliaria",

    'summary': """
        Modelo de inmobiliaria""",

    'description': """
        Podras gestionar tus acciones de clientes, empleados y ventas
    """,

    'author': "Ismael-13",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #FICHERO DE SEGURIDAD PARA DAR PERMISOS A LAS VISTAS/MODULOS
        'security/ir.model.access.csv',
        #VISTAS QUE ODOO TENDRA EN CUENTA PARA EL MODULO
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
