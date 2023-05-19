from odoo import api, fields, models

class OwlTodo(models.Model):
    _name = 'owl.todo.list'
    _description = 'OWL Todo Application'
    # _rec_name = 'country'

    name = fields.Char(string="Task Name")
    completed = fields.Boolean()
    color = fields.Char()
    capitalized_name = fields.Char(string='Capitalized Name', compute="_compute_capitalized_name", store=True)
    country = fields.Char(string="Country")
    active = fields.Boolean(default=True)
    tag_ids = fields.Many2many('res.partner.category', 'school_tag_relation', 'school_id', 'tag_id', string="Tags")
    appointment_date = fields.Date(string="date")

    @api.depends('name')
    def _compute_capitalized_name(self):
        if self.name:
            self.capitalized_name = self.name.upper()
        else:
            self.capitalized_name = ''


    def name_get(self):
        res = []
        for rec in self:
            name = f'{rec.capitalized_name} - {rec.country}'
            res.append((rec.id, name))
        return res
