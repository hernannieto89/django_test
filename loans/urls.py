"""
Loans app url module
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'manager/', views.manager, name='manager'),
]
