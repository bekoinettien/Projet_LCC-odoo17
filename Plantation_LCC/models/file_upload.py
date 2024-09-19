from odoo import models, fields, api
import base64
import os
# import sys
# sys.path.append('/usr/lib/python3/dist-packages/demo')
import msoffcrypto

class FileUpload(models.Model):
    _name = 'file.upload'
    _description = 'File Upload'

    file_data = fields.Binary(string='File', required=True)

    @api.model
    def create(self, vals):
        record = super(FileUpload, self).create(vals)
        if record.file_data:
            self.save_file_to_disk(record.file_data)
        return record

    def save_file_to_disk(self, file_data):
        decoded_file = base64.b64decode(file_data)
        fixed_file_name = "lcctemporyfile.xlsx"
        file_path = os.path.join('D:\Odoo17\crypto', fixed_file_name)  # Change the path to your desired directory

        with open(file_path, 'wb') as file:
            file.write(decoded_file)

        fichier_crypter = open(r"D:\Odoo17\crypto\lcctemporyfile.xlsx", "rb")
        file = msoffcrypto.OfficeFile(fichier_crypter)
        file.load_key(password="IPACRCI")
        with open(r"D:\Odoo17\server\odoo\addons\documents\decrypter.xlsx", "wb") as f:
         file.decrypt(f)

        return fixed_file_name


