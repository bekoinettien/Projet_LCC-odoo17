# from odoo import models, fields, api
# import win32com.client as win32
#
# class ExcelPasswordRemoval(models.Model):
#     _name = 'excel.password.removal'
#     _description = 'Remove password from Excel files'
#
#     name = fields.Char(string='File Name', required=True)
#     password = fields.Char(string='Password')
#
#     def remove_password(self):
#         for record in self:
#             try:
#                 filename = record.name
#                 pw_str = record.password
#                 xcl = win32.Dispatch("Excel.Application")
#                 wb = xcl.Workbooks.Open(filename, False, False, None, pw_str)
#                 xcl.DisplayAlerts = False
#                 wb.SaveAs(filename, None, '', '')
#                 wb.Close(SaveChanges=False)
#                 xcl.Quit()
#                 record.message_post(body="Mot de passe supprimé avec succès.")
#             except Exception as e:
#                 record.message_post(body=f"Une erreur s'est produite : {e}")
#

from odoo import models, fields, api
import base64
import tempfile
import win32com.client as win32
import pandas as pd
from odoo.exceptions import UserError

class ExcelImportWizard(models.TransientModel):
    _name = 'excel.import.wizard'
    _description = 'Wizard for importing Excel files'

    file = fields.Binary(string='Excel File', required=True)
    filename = fields.Char(string='File Name')

    def import_file(self):
        for record in self:
            # Save the uploaded file to a temporary location
            file_content = base64.b64decode(record.file)
            temp_file_path = tempfile.mktemp(suffix=".xlsx")
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(file_content)

            # Remove password from the file
            self.remove_password(temp_file_path)

            # Import the Excel file
            self.process_file(temp_file_path)

    def remove_password(self, filename):
        password = 'IPACRCI'
        try:
            xcl = win32.Dispatch("Excel.Application")
            wb = xcl.Workbooks.Open(filename, False, False, None, password)
            xcl.DisplayAlerts = False
            wb.SaveAs(filename, None, '', '')
            wb.Close(SaveChanges=False)
            xcl.Quit()
        except Exception as e:
            raise UserError(f"Une erreur s'est produite lors de la suppression du mot de passe : {e}")

    def process_file(self, file_path):
        try:
            df = pd.read_excel(file_path)
            # Process the DataFrame (df) as needed
            for index, row in df.iterrows():
                # Example: create a record in a model 'excel.file.content'
                self.env['excel.file.content'].create({
                    'column1': row['Column1'],
                    'column2': row['Column2'],
                    # Add other fields as needed
                })
            raise UserError("Fichier importé avec succès.")
        except Exception as e:
            raise UserError(f"Une erreur s'est produite lors de l'importation du fichier : {e}")


