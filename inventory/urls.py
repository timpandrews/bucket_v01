from django.conf.urls import url
from django.contrib import admin

from inventory.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
]