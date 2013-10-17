
from osv import fields, osv

class account_invoice_custom(osv.osv):
    _name='account.invoice'
    _inherit='account.invoice'
    
    def invoice_print(self, cr, uid, ids, context=None):
        res = super(account_invoice_custom, self).invoice_print( cr, uid, ids,context)
        res["report_name"] = "report.account.invoice.custom"
        return res

account_invoice_custom()
