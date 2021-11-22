from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns=[
    path('ashu/',ashu,name='ashu'),
    path('nikky/',nikky,name='nikky'),
]