{
    'name': 'mydemo',
    'author': 'Dmitriy Chumak',
    'website': 'http://www.dmitriy.chumak.com',
    'version': '17.0.0.0.1',
    'summary': 'I want to learn odoo',
    'description': 'this module is used to learn odoo',
    'category': 'Customization',
    'license': 'OPL-1',
    'depends': [
                'base',
                ],
    'data': [
        'view/my_demo_views.xml'
    ],

    'demo': [''],
    'installable': True,
    'auto_install': False,
    'application': False,
    'external_dependencies': {
        'python': [''],
    },

    'images': [
        'static/description/icon.png'
    ],

    'price': 0,
    'currency': 'EUR',
}