# -*- coding: utf-8 -*-
{
    'name': "Gestion taller",

    'summary': """
        Practica Odoo 15 para gestion de taller
        """,

    'description': """
        Practica Odoo 15 para gestion de taller
    """,

    'author': "PROSERT SRL",
    'website': "http://www.prosertrd.com",

    'category': 'Uncategorized',
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/car_view.xml',
        #'views/templates.xml',
    ],

}
