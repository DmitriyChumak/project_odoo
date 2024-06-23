{
    'name': 'Hospital management ',
    'version': '17.0.0.0.1',
    'summary': 'This is module should help hospital management',

    'category': 'Healthcare',
    'author': 'Dmitriy Chumak',
    'license': 'AGPL-3',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/hr_hospital_menu.xml',
        'data/master_data.xml',
    ],

    'demo': [
        'demo/demo_data.xml',
    ],

    'external_dependencies': {

    },

    'installable': True,
    'auto_install': False,
    'application': True,



    'price': 0,
    'currency': 'EUR',
}
