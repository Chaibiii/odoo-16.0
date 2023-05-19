from odoo import api, fields, models

class SchoolManagement(models.Model):
    _name = 'school.management'

    name = fields.Char(string="Name")
    country = fields.Char(string="Country")
    todo_id = fields.Many2one('owl.todo.list', string="Task Name")
