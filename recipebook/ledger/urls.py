# <appname>/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]

app_name = 'ledger'