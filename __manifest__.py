# -*- coding: utf-8 -*-
{
    'name': "DyD",

    'summary': """Ejercicio final de Sistemas de Gestión Empresarial""",

    'description': """ Generador de personajes para Dungeon & Dragons 3.5""",

    'author': "Agil Centros",
    'website': "https://github.com/DrackPyros",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
