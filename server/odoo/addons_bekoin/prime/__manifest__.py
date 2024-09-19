{
    'name': 'Prime exceptionnelle',
    'version': '1.0',
    'sequence': '-10',
    'summary': 'Prime',
    'description':"""
    Ce module facilite la gestion de la paie planteur dans Odoo
    - donne une prime exceptionnelle
    - Lot de paie et calcule de faie de paie
    - Gestion de la paie par zone
    - Gestion des virements par zone
    - Rapport de suivi de paie
    - Generation automatique des ecritures comptables par periode paie
    - Configuration des journaux
    ====================================================
""",
    'category': 'Services/',
    'author': 'Hamko',
    'website': 'https://www.integrateur.odoo.com',
    'depends': ['base','account' , 'plantation'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/prime_excep.xml',
        'wizard/prime_excep_wizard_view.xml',
        'menus/prime_excep.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
