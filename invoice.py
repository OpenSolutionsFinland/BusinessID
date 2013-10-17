from osv import osv, fields

class account_invoice_custom(osv.osv):
    _name='account.invoice'
    _inherit='account.invoice'
    
    _columns = {}
    
    def invoice_print(self, cr, uid, ids, context=None):
        res = super(account_invoice_custom, self).invoice_print( cr, uid, ids,context)
        res["report_name"] = "account.invoice.custom"
        return res

account_invoice_custom()
