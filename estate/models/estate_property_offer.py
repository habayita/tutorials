from odoo import api, fields, models
from datetime import date
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
	_name = "estate.property.offer"
	_description = "estate property offers"

	price = fields.Float()
	status = fields.Selection(selection=[('Accepted', 'accepted'), ('Refused', 'refused')], copy=False)
	partner_id = fields.Many2one("res.partner", string='Partner', required=True)
	property_id = fields.Many2one("estate.property", required=True)
	validity = fields.Integer(string="Validity (days)", default=7)
	date_deadline = fields.Date(string="Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")


	@api.depends("validity", "create_date")
	def _compute_date_deadline(self):
		for record in self:
			base_date = record.create_date.date() if record.create_date else fields.Date.context_today(record)
			record.date_deadline = base_date + relativedelta(days=record.validity)

	def _inverse_date_deadline(self):
		for record in self:
			base_date = record.create_date.date() if record.create_date else fields.Date.context_today(record)
			record.validity = (record.date_deadline - base_date).days