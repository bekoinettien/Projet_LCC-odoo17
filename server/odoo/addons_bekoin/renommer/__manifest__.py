{
    'name': 'telechargement de fichier',
    'version': '1.0',
    'sequence': '3',
    'summary': 'Telechargement du fichier sur le disk',
    'author': 'BEKOIN',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/file_upload_view.xml',
    ],
    'installable': True,
    'application': True,
}
