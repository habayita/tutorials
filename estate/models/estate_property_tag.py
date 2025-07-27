from odoo import fields, models 

class EstatePropertyTag(models.Model):
	_name = "estate.property.tag"
	_description = "estate property tag"
	_order = "name"

	name = fields.Char(required=True)
	color = fields.Integer()

	_sql_constraints = [
        ('unique_tag_name', 'UNIQUE(name)', 'The tag name nust be unique.')
    ]