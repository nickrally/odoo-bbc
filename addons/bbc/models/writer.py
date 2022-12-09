from odoo import api, models, fields

class Writer(models.Model):
    _name = "bbc.writer"
    _rec_name = 'name'

    name = fields.Char(string="Name")
    country = fields.Char(string="Country")