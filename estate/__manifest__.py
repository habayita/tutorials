{
	'name': 'Estate',
	'version': '1.0',
	'author': 'efrat',
	'depends': ['base'],
	'installable': True,
	'application': True,
	'data': [
		'views/estate_property_views.xml',
		'views/estate_property_menus.xml',
		'views/estate_property_type_views.xml',
		'views/estate_property_type_menus.xml',
		'views/estate_property_tag_views.xml',
		'views/estate_property_tag_menus.xml',
		'views/estate_property_offer_views.xml',
		'security/ir.model.access.csv',
	],
}
