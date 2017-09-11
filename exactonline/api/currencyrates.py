# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for ledgeraccount resources.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015 Walter Doekes, OSSO B.V.
"""
from .manager import Manager


class CurrencyRates(Manager):
    resource = 'financial/ExchangeRates'

    def filter(self, **kwargs):
        if 'select' not in kwargs:
            kwargs['select'] = 'StartDate,SourceCurrency,TargetCurrency,Rate'
        return super(CurrencyRates, self).filter(**kwargs)

