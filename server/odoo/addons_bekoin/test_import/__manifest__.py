{
    'name': 'Custom Module',
    'version': '1.0',
    'summary': 'Module personnalisé pour importer des fichiers',
    'author': 'BEKOIN',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'wizard/import_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}
