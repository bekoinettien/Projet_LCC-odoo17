from odoo import models, fields

class ExcelFileContent(models.Model):
    _name = 'excel.file.content'
    _description = 'Content of the imported Excel file'

    column1 = fields.Char(string='Column 1')
    column2 = fields.Char(string='Column 2')
    # Add other fields as needed
