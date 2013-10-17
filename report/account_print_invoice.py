# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP
#    Copyright (C) 2013 
#
##############################################################################
import time
from openerp.report import report_sxw

class account_invoice_finland(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(account_invoice_finland, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })

report_sxw.report_sxw(
    'report.account.invoice.custom',
    'account.invoice',
    'addons/business_id_finland/report/account_print_invoice.rml',
    parser=account_invoice_finland
)
