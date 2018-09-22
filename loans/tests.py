# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import IntegrityError
from .models import LoanRequest


class LoanRequestTestCase(TestCase):
    """
    LoanRequest model testcase.
    """

    def setUp(self):
        LoanRequest.objects.create(dni="23454535", first_name="foo", last_name="bar",
                                   email="a@a.com", loan_amount=1232, gender="F")

    def test_loan_request_approval_status_default(self):
        """Loan request instance has false approval_status by default."""
        loan_request = LoanRequest.objects.get(dni="23454535")
        self.assertFalse(loan_request.approval_status)

    def test_unique_dni_loan_request_constraint(self):
        """Loan request instance dni field has an unique constraint."""
        with self.assertRaises(IntegrityError):
            LoanRequest.objects.create(dni="23454535", first_name="foo2",
                                       last_name="bar2", email="a@a.com",
                                       loan_amount=1232, gender="M")
