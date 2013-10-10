from osv import fields, osv

class business_id(osv.osv):
	_name='res.partner'
	_inherit='res.partner'

	_columns= {
		'business_id_finland': fields.char('Business ID', required=False)
		
	}

business_id()

