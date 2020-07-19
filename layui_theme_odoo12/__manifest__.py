# -*- coding: utf-8 -*-
{
    'name': "layui_theme_odoo12",

    'summary': """
        odoo12的layui主题""",

    'description': """
        odoo12的layui主题
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'base_import'],
    'qweb': [
      'static/xml/*.xml'
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/assets.xml',
        'views/extend_view/layout.xml',
        'views/extend_view/login.xml',
        'views/config_view.xml',
    ],
    'application': True
}