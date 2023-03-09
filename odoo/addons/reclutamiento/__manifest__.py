
{
    'name': "reclutamiento",

    'summary': """
          Es un modelo para reclutar tropas romanas """,

    'description': """
        Si quieres reclutar tropas romanas y gestionar sus ejercitos, este es tu modulo
    """,

    'author': "Alvaro Caña",
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
    'application' : True
}
