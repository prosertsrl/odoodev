# -*- coding: utf-8 -*-
{
    'name': "Votantes",

    'summary': """
        Aplicación para la gestion de votantes""",

    'description': """
        Aplicación para la gestion de votantes
    """,

    'author': "PROSERT SRL",
    'website': "https://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
