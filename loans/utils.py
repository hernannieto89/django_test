"""
Loans app utils module.
"""
import requests

from django.conf import settings

from .models import LoanRequest


def approve_loan(document_number, gender, email):
    """
    Approves loan. Uses VALIDATION_ENDPOINT.
    :param document_number: string
    :param gender: string
    :param email: string
    :return: boolean
    """
    result = False
    endpoint = settings.VALIDATION_ENDPOINT
    response = requests.get(endpoint.format(document_number, gender, email))
    if response.status_code == 200:
        result = response.json()['approved']
    loan_request, _ = LoanRequest.objects.get_or_create(dni=document_number)
    loan_request.approval_status = result
    loan_request.save()
    return result


def check_loan_status(loan_request, new):
    """
    Checks loan status. Creates an according message.
    :param loan_request: LoanRequest
    :param new: boolean
    :return: string
    """
    msg = ''
    if not new:
        msg = '{0} Loan with the same DNI found. {1}'
        if loan_request.approval_status:
            msg = msg.format('Approved', 'Wait for cashing out before asking a new one.')
        else:
            msg = msg.format('Rejected', 'Please retry in a few days or call customer service.')
    return msg
