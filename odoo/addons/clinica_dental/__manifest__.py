# -*- coding: utf-8 -*-
{
    'name': "clinica_dental",

    'summary': """
        Modulo de gestion Clinica Dental
        """,

    'description': """
En este módulo se está creando una clínica dental.
Este módulo permitiría a los usuarios registrar pacientes, crear citas 
dentales, asignar profesionales dentales a las citas y llevar un registro 
de los tratamientos realizados en los pacientes.

El módulo también permite registrar seguros médicos y asociarlos 
a pacientes, lo que puede ser útil para la facturación y el 
seguimiento de los pagos. Además, el módulo ofrece una funcionalidad 
para agregar procedimientos a los tratamientos y calcular el costo total del tratamiento.

    """,

    'author': "Clinica_Dental.AdrianBlanco",
    'website': "https://github.com/Chuny2/",

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
}
