from osv import fields, osv

class product_extension(osv.osv):
	_name='product.product'
	_inherit='product.product'

	_columns= {
		'quality_check_text': fields.text('Quality check text', required=False),
		'quality_lower_limit': fields.float('Lower Limit', required=False),
		'quality_upper_limit': fields.float('Upper Limit', required=False)
	}

product_extension()

