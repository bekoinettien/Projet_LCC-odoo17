# custom_module/models/custom_model.py
import os
import base64
import sys
sys.path.append('/usr/lib/python3/dist-packages/demo')
import pandas as pd
from odoo import models, fields, api

class CustomModule(models.Model):
    _name = 'custom.module'
    _description = 'Custom Module'

    name = fields.Char(string="Name")
    file_data = fields.Binary(string="File")
    file_name = fields.Char(string="File Name")

    @api.model
    def create(self, vals):
        record = super(CustomModule, self).create(vals)
        if vals.get('file_data'):
            self.process_file(vals['file_data'])
        return record

    def process_file(self, file_data):
        file_content = base64.b64decode(file_data)
        # Traitez le fichier Excel ici avec pandas
        df = pd.read_excel(file_content)

        print(df.head())

    @api.model
    def import_files_from_demo_folder(self):
        demo_folder_path = '/cryptage'  # Remplacez par le chemin réel
        for file_name in os.listdir(demo_folder_path):
            if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
                file_path = os.path.join(demo_folder_path, file_name)
                with open(file_path, 'rb') as file:
                    file_data = file.read()
                    self.create({
                        'name': file_name,
                        'file_name': file_name,
                        'file_data': base64.b64encode(file_data).decode('utf-8')
                    })
