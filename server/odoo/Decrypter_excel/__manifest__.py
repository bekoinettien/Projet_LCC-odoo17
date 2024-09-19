# __manifest__.py
{
    'name': 'Excel Decryptor',
    'version': '1.0',
    'sequence': '2S',
    'summary': 'Decrypt Excel files in Odoo',
    'description': 'Module to decrypt and read Excel files protected by a password in Odoo 17',
    'author': 'Votre Nom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/excel_decryptor_view.xml',
        'views/menu_view.xml',
        'wizard/decrypt_excel_wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}
