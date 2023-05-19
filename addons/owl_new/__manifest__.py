# -*- coding: utf-8 -*-
{
    'name': "owl_new",

    'description': """
    """,
    'category': 'Productivity',
    'version': '0.1',
    'sequence': '-1',
    'depends': ['base', 'web'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
        'views/school.xml',
    ],
    'assets': {
        'web.assets_backend': [
          # 'owl_new/static/src/components/*/*.js',
          # 'owl_new/static/src/components/*/*.xml',
          # 'owl_new/static/src/components/*/*.scss',
        ],
    }
}
