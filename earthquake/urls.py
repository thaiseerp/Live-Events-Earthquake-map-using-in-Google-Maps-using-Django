"""
Author: Thaiseer Parammal
"""

from django.conf.urls import url
from . import views
from . import google_earth

app_name = 'earthquake'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

google_earth.write_to_kml()
