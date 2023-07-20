# -*- coding: utf-8 -*-
{
    'name': "Gestion Taller",

    'summary': """
        Modulo para la gestion de reparaciones de vehiculos en el taller""",

    'description': """
        Practica curso odoo 15 Tecnico para gestion de taller
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
        'data/brands.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/car_views.xml',
    ],
}