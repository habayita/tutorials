from odoo import api, fields, models
from datetime import date 
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class EstateProperty(models.Model):
	_name = "estate.property"
	_description = "estate property"

	name = fields.Char(required=True)
	description = fields.Text()
	postcode = fields.Char()
	date_availability = fields.Date(copy=False, default= date.today() + relativedelta(months=3))
	expected_price = fields.Float(required=True)
	selling_price = fields.Float(readonly=True, copy=False)
	bedrooms = fields.Integer(default=2)
	living_area = fields.Integer()
	facades = fields.Integer()
	garage = fields.Boolean()
	garden = fields.Boolean()
	garden_area = fields.Integer()
	garden_orientation = fields.Selection(string='Garden Orientation', selection=[('North', 'north'), ('South', 'south'), ('East', 'east'), ('West', 'west')])
	active = fields.Boolean(default=True)
	state = fields.Selection(string='Status', selection=[('New', 'new'),('Offer Received', 'offer received'),('Offer Accepted', 'offer accepted'),('Sold', 'sold'),('Cancelled', 'cancelled')], required=True, copy=False, default='New')
	property_type_id = fields.Many2one("estate.property.type", string="Property Type")
	salesman_id = fields.Many2one("res.users", string='Salesman', default= lambda self: self.env.user)
	buyer_id = fields.Many2one("res.partner", string='Buyer', copy=False)
	tag_ids = fields.Many2many("estate.property.tag", string='Tags')
	offer_ids = fields.One2many("estate.property.offer", "property_id")
	total_area = fields.Integer(compute="_compute_total_area")
	best_offer = fields.Float(compute="_compute_best_offer")

	@api.depends("living_area", "garden_area")
	def _compute_total_area(self):
		for record in self:
			record.total_area = record.living_area + record.garden_area

	@api.depends("offer_ids.price")
	def _compute_best_offer(self):
		for record in self:
			record.best_offer = max(record.offer_ids.mapped("price"), default=0.0)

	@api.onchange("garden")
	def _onchange_garden(self):
		if self.garden is True:
			self.garden_area=10
			self.garden_orientation='North'
		else:
			self.garden_area=0
			self.garden_orientation=False

	
	def action_sold_button(self):
		for record in self:
			if self.state != 'Cancelled':
				self.state = 'Sold'
			else:
				raise UserError('Cancelled properties cannot be sold')
			return True
	
	def action_cancel_button(self):
		for record in self:
			if self.state != 'Sold':
				self.state = 'Cancelled'
			else:
				raise UserError('Sold properties cannot be cancelled')
			return True