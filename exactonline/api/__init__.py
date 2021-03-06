# vim: set ts=8 sw=4 sts=4 et ai tw=79:
"""
Combines the helper superclasses and the helper resource managers into the
ExactApi class.

This file is part of the Exact Online REST API Library in Python
(EORALP), licensed under the LGPLv3+.
Copyright (C) 2015 Walter Doekes, OSSO B.V.
"""
from ..rawapi import ExactRawApi

from .autorefresh import Autorefresh
from .unwrap import Unwrap
from .v1division import V1Division

from .contacts import Contacts
from .invoices import Invoices
from .ledgeraccounts import LedgerAccounts
from .receivables import Receivables
from .relations import Relations
from .payables import Payables
from .journals import Journals
from .transaction_lines import TransactionLines
from .transactions import Transactions
from .currencyrates import CurrencyRates


class ExactApi(
    # Talk to /api/v1/{division} directly.
    V1Division,
    # Strip the surrounding "d" and "results" dictionary
    # items.
    Unwrap,
    # Ensure that tokens are refreshed: if we get a 401, refresh the
    # tokens.
    Autorefresh,
    # The base class comes last: talk to /api.
    ExactRawApi
):
    contacts = Contacts.as_property()
    invoices = Invoices.as_property()
    ledgeraccounts = LedgerAccounts.as_property()
    receivables = Receivables.as_property()
    relations = Relations.as_property()
    payables = Payables.as_property()
    journals = Journals.as_property()
    transactions = Transactions.as_property()
    transaction_lines = TransactionLines.as_property()
    currency_rates = CurrencyRates.as_property()
