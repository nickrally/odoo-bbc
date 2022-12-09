from odoo import api, models, fields

class Book(models.Model):
    _name = "bbc.book"

    title = fields.Char(string="Title")
    writer = fields.Many2one('bbc.writer', string='Writer')