# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for transactions resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class Transactions(Manager):
    """
    Transactions objects
    """
    resource = 'financialtransaction/Transactions'

    def filter(self, date__lt=None, date__gt=None, **kwargs):
        if 'select' not in kwargs:
            select = [
                'EntryID',
                'TransactionLines',
                'Type',
                'ClosingBalanceFC',
                'Date',
                'OpeningBalanceFC',
                'FinancialYear',
                'FinancialPeriod',
            ]
            kwargs['select'] = ','.join(select)
        if date__lt is not None:
            self._filter_append(kwargs, "Date lt {}".format(
                self._remote_datetime(date__lt)))
        if date__gt is not None:
            self._filter_append(kwargs, "Date gt {}".format(
                self._remote_datetime(date__gt)))
        return super().filter(**kwargs)
