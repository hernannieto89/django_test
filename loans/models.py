# -*- coding: utf-8 -*-
"""
Loans app models module.
"""
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MinValueValidator


class LoanRequest(models.Model):
    """
    Loan Request model
    """
    dni = models.CharField(max_length=200, null=True, unique=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=200, null=True)
    loan_amount = models.FloatField(validators=[MinValueValidator(0)], null=True)
    approval_status = models.BooleanField(default=False)
