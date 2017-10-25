# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for transaction lines resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class TransactionLines(Manager):
    """
    Transaction lines
    """
    resource = 'financialtransaction/TransactionLines'

    def filter(self, invoice_id__in=None, date__lt=None, date__gt=None,
               account_code__in=None, type__in=None, **kwargs):
        if 'select' not in kwargs:
            select = [
                'Account',
                'AccountCode',
                'AmountDC',
                'AmountVATBaseFC',
                'Date',
                'DueDate',
                'Created',
                'Division',
                'FinancialYear',
                'FinancialPeriod',
                'EntryID',
                'EntryNumber',
                'GLAccount',
                'GLAccountCode',
                'ID',
                'JournalCode',
                'Type',
                'VATPercentage',
                'VATCode',
                'VATType',
                'VATCodeDescription',
            ]
            kwargs['select'] = ','.join(select)
        if date__lt is not None:
            self._filter_append(kwargs, "Date lt {}".format(
                self._remote_datetime(date__lt)))
        if date__gt is not None:
            self._filter_append(kwargs, "Date gt {}".format(
                self._remote_datetime(date__gt)))
        if invoice_id__in is not None:
            invoice_filter = []
            for invoice_id in invoice_id__in:
                invoice_filter.append(
                    "InvoiceNumber eq '{}'".format(invoice_id))
            if len(invoice_filter) > 0:
                self._filter_append(
                    kwargs, '({})'.format(' or '.join(invoice_filter)))
        if account_code__in is not None:
            accounts_filter = []
            for account_code in account_code__in:
                accounts_filter.append(
                    "GLAccountCode eq '{}'".format(account_code))
            if len(accounts_filter) > 0:
                self._filter_append(
                    kwargs, '({})'.format(' or '.join(accounts_filter)))
        if type__in is not None:
            types_filter = []
            for t_type in type__in:
                types_filter.append(
                    "Type eq {}".format(t_type))
            if len(types_filter) > 0:
                self._filter_append(
                    kwargs, '({})'.format(' or '.join(types_filter)))
        return super().filter(**kwargs)
