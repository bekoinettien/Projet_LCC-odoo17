# custom_module/__manifest__.py
{
    'name': 'Custom Module',
    'version': '1.0',
    'summary': 'Module to import Excel files from server folder DEMO',
    'author': 'ETTIEN',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/custom_view.xml',
        'data/ir_cron_data.xml',
    ],
    'installable': True,
    'application': True,
}
