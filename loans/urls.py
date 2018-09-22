"""
Loans app url module
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'manager/', views.manager, name='manager'),
    url(r'delete/(?P<dni>[\w]+)/$', views.delete_request, name='delete_request'),
    url(r'logout/', views.manager_logout, name='manager_logout'),

]
