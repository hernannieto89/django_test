# -*- coding: utf-8 -*-
"""
Loans app forms module.
"""
from django.forms import ModelForm, ValidationError
from loans.models import LoanRequest


class LoanRequestForm(ModelForm):
    """
    Loan request form.
    """
    class Meta:
        model = LoanRequest
        fields = ['dni', 'first_name', 'last_name', 'email', 'gender', 'loan_amount']

    def clean(self):
        cleaned_data = super(LoanRequestForm, self).clean()
        email = cleaned_data.get('email')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        gender = cleaned_data.get('gender')
        dni = cleaned_data.get('dni')
        loan_amount = cleaned_data.get('loan_amount')
        if not all([email, first_name, last_name, gender, dni, loan_amount]):
            raise ValidationError('All fields are mandatory!')


class EditionLoanRequestForm(LoanRequestForm):
    """
    Edition loan request form.
    """
    class Meta:
        model = LoanRequest
        fields = ['dni', 'first_name', 'last_name', 'email',
                  'gender', 'loan_amount', 'approval_status']
