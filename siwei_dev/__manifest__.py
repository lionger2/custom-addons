# -*- coding: utf-8 -*-
{
    'name': "siwei_dev",

    'summary': """
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Huang siwei",
    'website': "http://www.huangsiwei.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Huang siwei',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['anodoo_base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/base_views.xml',
        'views/siwei_dev_menu.xml',
        'views/siwei_dev_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
