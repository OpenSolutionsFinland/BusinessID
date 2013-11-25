from osv import fields, osv
from openerp.tools.translate import _

class business_id(osv.osv):
	_name='res.partner'
	_inherit='res.partner'

	_columns= {
		'business_id_finland': fields.char('Business ID', required=False),
        'wtf_id': fields.char('Maventa ID', required=False)
	}

business_id()
