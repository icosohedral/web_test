from django.conf.urls import *
from django.urls import re_path
from .api import api

urlpatterns = [
    #re_path(r'^api/bhpwd$', api.bPWD),
    #re_path(r'^api/bhsess$', api.bSess),
    re_path(r'^test$', api.test),
]
