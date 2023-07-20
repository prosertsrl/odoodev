# -*- coding: utf-8 -*-
{
    'name': "Gestion de Votantes",

    'summary': """
        Modulo para la gestion de votantes""",

    'description': """
        Seguimiento y contacto a los militantes del partido
    """,

    'author': "PROSERT SRL",
    'website': "http://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/provinces_views.xml',
    ],
}