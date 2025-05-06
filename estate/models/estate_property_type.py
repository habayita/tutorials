from odoo import fields, models

class EstatePropertyType(models.Model):
	_name = "estate.property.type"
	_description = "estate property type"
	_order = "name"

	name = fields.Char(required=True)
	property_ids = fields.One2many('estate.property', 'property_type_id')
	sequence = fields.Integer(default=1, help="Used to order stages. Lower is better.")

	_sql_constraints = [
        ('unique_type_name', 'UNIQUE(name)', 'The type name nust be unique.')
    ]