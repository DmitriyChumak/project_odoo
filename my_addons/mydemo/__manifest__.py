{
    'name': 'My super demo module',
    'version': '17.0.0.0.1',
    'summary': 'This is a demo module',
    'description': '',

    'category': 'Customization',
    'author': 'Dmitriy Chumak',
    'website': 'dmitriy.chumak.com',

    'license': 'OPL-1',
    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/my_demo_views.xml',
        ],

    'demo': [''],

    'installable': True,
    'auto_install': False,
    'application': True,
    'external_dependencies': {

    },


    'images': ['static/description/icon.png'],
    'price': 0,
    'currency': 'EUR'
}