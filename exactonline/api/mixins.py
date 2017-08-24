class DueDateFilter:
    def filter(self, pk=None, relation_id=None, duedate__lt=None, duedate__gt=None,
               enddate__gt_or_null=None, **kwargs):
        """
        A common query would be duedate__lt=date(2015, 1, 1) to get all
        Receivables that are due in 2014 and earlier.
        """
        if 'select' not in kwargs:
            select = [
                'ID',
                'AmountDC',
                'AmountDiscountDC',
                'AccountName',
                'BankAccountID',
                'DueDate',
                'DiscountDueDate',
                'EndDate',
                'EntryDate',
                'EntryNumber',
                'InvoiceDate',
                'PaymentDays',
                'PaymentDaysDiscount',
                'PaymentMethod',
                'Status',
                'TransactionAmountDC',
                'TransactionEntryID',
                'TransactionID',
                'TransactionType',
                'Modified',
            ]
            kwargs['select'] = ','.join(select)

        if pk is not None:
            pk = self._remote_guid(pk)
            self._filter_append(kwargs, u'ID eq %s' % (pk,))

        if relation_id is not None:
            # Filter by (relation) account_id. There doesn't seem to be
            # any reason to prefer
            # 'read/financial/ReceivablesListByAccount?accountId=X' over
            # this.
            relation_id = self._remote_guid(relation_id)
            self._filter_append(kwargs, u'AccountId eq %s' % (relation_id,))

        if duedate__lt is not None:
            # Not sure what the AgeGroup means in
            # ReceivablesListByAgeGroup, but we can certainly do
            # without.
            duedate__lt = self._remote_datetime(duedate__lt)
            self._filter_append(kwargs, u'DueDate lt %s' % (duedate__lt,))

        if duedate__gt is not None:
            # Not sure what the AgeGroup means in
            # ReceivablesListByAgeGroup, but we can certainly do
            # without.
            duedate__gt = self._remote_datetime(duedate__gt)
            self._filter_append(kwargs, u'DueDate gt %s' % (duedate__gt,))

        if enddate__gt_or_null is not None:
            enddate__gt = self._remote_datetime(enddate__gt_or_null)
            self._filter_append(
                kwargs,
                u'(EndDate gt %s or EndDate eq null)' % (enddate__gt)
            )

        return super().filter(**kwargs)
