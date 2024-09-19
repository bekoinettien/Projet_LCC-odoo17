# models/decrypt_excel_wizard.py
from odoo import models, fields, api

class DecryptExcelWizard(models.TransientModel):
    _name = 'decrypt.excel.wizard'
    _description = 'Wizard to Decrypt Excel File'

    file = fields.Binary(string='File', required=True)
    file_name = fields.Char(string='File Name')
    password = fields.Char(string='Password', required=True)

    def action_decrypt(self):
        decryptor = self.env['excel.decryptor'].create({
            'file': self.file,
            'file_name': self.file_name,
            'password': self.password,
        })
        decryptor.action_decrypt_and_view()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Decrypted File',
            'res_model': 'excel.decryptor',
            'view_mode': 'form',
            'res_id': decryptor.id,
            'target': 'new',
        }
