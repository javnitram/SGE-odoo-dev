{
    'name': "Pokemodulo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Primer modulo de Alonso Rivas Alcobendas,
        consisten en la gestión y creación de equipos 
        sencillos y de entrenadores de pokemon
    """,

    'author': "Rivas Alcobendas Alonso",


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
