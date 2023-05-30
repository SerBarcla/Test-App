{
    'name': 'My Odoo App',
    'version': '1.0',
    'summary': 'An app to input date and description',
    'icon': 'icon.png',
    'description': 'A custom Odoo app that takes a date and description as input',
    'author': 'Your Name',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'views/app_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
