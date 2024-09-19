from odoo import models, fields, api

class ImportWizard(models.TransientModel):
    _name = 'import.wizard'
    _description = 'Import Wizard'

    def import_action(self):
        import_file_model = self.env['import.file']
        import_file_model.import_files()
