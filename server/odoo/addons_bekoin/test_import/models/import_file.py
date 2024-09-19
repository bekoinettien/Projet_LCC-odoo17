import os
from odoo import models, fields, api
import sys
sys.path.append('/usr/lib/python3/dist-packages/demo')
import openpyxl

class ImportFile(models.Model):
    _name = 'import.file'
    _description = 'Import File'

    file = fields.Binary(string="File", required=True)
    def import_files(self):
        file_path = '/cryptage/decrypter.xlsx'  # Chemin vers le fichier sur le serveur

        if os.path.exists(file_path):

            workbook = openpyxl.load_workbook(file_path)
            sheet = workbook.active

            for row in sheet.iter_rows(values_only=True):
                # Traitez les lignes du fichier Excel
                self.create({'name': row[0]})
        else:
            raise FileNotFoundError(f"The file {file_path} does not exist.")

# class ImportFile(models.Model):
#     _name = 'import.file'
#     _description = 'Import File'
#
#     name = fields.Char(string='Name')
#
#     def import_files(self):
#         file_path = '/cryptage/decrypter.csv'  # Chemin vers le fichier sur le serveur
#
#         if os.path.exists(file_path):
#             with open(file_path, 'r', encoding='latin-1') as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#                     # Traitez les lignes du fichier CSV
#                     self.create({'name': row[0]})
#         else:
#             raise FileNotFoundError(f"The file {file_path} does not exist.")
