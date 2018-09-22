# -*- coding: utf-8 -*-
"""
Loans app views module.
"""
from __future__ import unicode_literals


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.admin.views.decorators import staff_member_required

from .forms import LoanRequestForm, EditionLoanRequestForm

from .models import LoanRequest

from .utils import check_loan_status, approve_loan


def index(request):
    """
    Index view for loans app.
    :param request: request instance
    :return: HttpResponse
    """
    if request.method == 'POST':
        loan_request, new = LoanRequest.objects.get_or_create(dni=request.POST['dni'])
        msg = check_loan_status(loan_request, new)
        form = LoanRequestForm(request.POST, instance=loan_request)
        if msg:
            messages.success(request, msg)
        else:
            if form.is_valid():
                form.save()
                if approve_loan(request.POST['dni'], request.POST['gender'], request.POST['email']):
                    messages.success(request, 'Loan approved.')
                else:
                    messages.error(request, 'Loan rejected.')
    else:
        form = LoanRequestForm()
    return render(request, 'loans.html', {'form': form})


@staff_member_required
def manager(request):
    """
    Manager view for loans app.
    :param request: request instance
    :return: HttpResponse
    """
    loan_requests = LoanRequest.objects.all()
    if request.method == 'GET':
        form = EditionLoanRequestForm()
    else:
        if LoanRequest.objects.filter(dni=request.POST['dni']).exists():
            loan_request = LoanRequest.objects.get(dni=request.POST['dni'])
            form = EditionLoanRequestForm(request.POST, instance=loan_request)
            if form.is_valid():
                form.save()
                messages.success(request, 'Loan edited.')
        else:
            form = EditionLoanRequestForm()
            messages.error(request, 'Loan not found.')

    return render(request, 'manager.html', {'loan_requests': loan_requests, 'form': form})


def manager_logout(request):
    """
    Logout handler view for loans app
    :param request: request instance
    :return: HttpResponse
    """
    if request.method == 'GET':
        logout(request)
    return redirect('/loans')
