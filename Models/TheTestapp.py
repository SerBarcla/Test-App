from odoo import models, fields


class MyApp(models.Model):
    _name = 'my.app'
    _description = 'My App Model'

    date = fields.Date(string='Date', required=True)
    description = fields.Text(string='Description', required=True)
