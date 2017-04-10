# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Helper for receivables (invoices sent by you).

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015 Walter Doekes, OSSO B.V.
"""
from .manager import Manager
from .mixins import DueDateFilter


class Receivables(DueDateFilter, Manager):
    """
    Get the elements that make up the Financial Reporting of Outstanding
    Receivables, you call this.
    """
    resource = 'cashflow/Receivables'
