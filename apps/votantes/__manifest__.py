# -*- coding: utf-8 -*-
{
    'name': "Gestion de Votantes",

    'summary': """
        Voter management module""",

    'author': "PROSERT SRL",
    'website': "http://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/provinces_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
