from odoo import fields, models

class EstatePropertyType(models.Model):
	_name = "estate.property.type"
	_description = "estate property type"

	name = fields.Char(required=True)
	
	_sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'The type name nust be unique.')
    ]