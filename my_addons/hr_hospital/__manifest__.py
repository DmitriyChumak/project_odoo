# __manifest__.py
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Module for managing hospital operations',
    'author': 'Dmitriy',
    'website': 'http://www.example.com',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/disease_views.xml',
        'views/visit_views.xml',
        'views/hospital_menu.xml',
        'data/hr_hospital_data.xml'
    ],

    'demo': [
        'demo/hr_hospital_demo.xml',
    ],
    'installable': True,
    'application': True,
}
