# -*- coding: utf-8 -*-
{
    'name': "Библиотека",

    'summary': """Библиотека""",

    'description': """Приложение для учета книг""",

    'author': "Artur Apanasov",

    'license': "AGPL-3",

    'depends': ['base'],

    'application': True,

    'data': [
        'security/book_groups_access_rules.xml',
        'security/ir.model.access.csv',

        'views/book_views.xml',
        'views/menu_items_views.xml',
    ],
}