from osv import fields, osv

class business_id(osv.osv):
	_name='res.partner'
	_inherit='res.partner'

	_columns= {
		'business_id_finland': fields.char('Business ID', required=False)
		
	}

business_id()

class account_invoice(osv.osv):
    _inherit='account.invoice'
    _name='account.invoice'

    def invoice_print(self, cr, uid, ids, context=None):
        res = super(account_invoice, self).invoice_print( cr, uid, ids,context) #self, cr, uid, ids, context)
        res["report_name"] = "account.invoice.custom"
        return res

account_invoice()