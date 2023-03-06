# -*- coding: utf-8 -*-
{
    'name': "libreria",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

<<<<<<< HEAD
    'author': "Profe",
    'website': "https://site.educa.madrid.org/ies.elcanaveral.mostoles/",
=======
    'author': "My Company",
    'website': "http://www.yourcompany.com",
>>>>>>> ff821938758c0a4298fbccc1c7352ee046627224

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
<<<<<<< HEAD
    'application': True
=======
>>>>>>> ff821938758c0a4298fbccc1c7352ee046627224
}
