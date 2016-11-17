"""
Author: Thaiseer Parammal
"""

from django.conf.urls import include, url
from django.contrib import admin
from earthquake import views as main_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_view.home, name='home'),
    url(r'^earthquake/', include('earthquake.urls')),
    url(r'^landslide/', main_view.landslide, name='landslide'),
    url(r'^forest_fire/', main_view.forest_fire, name='forest_fire'),
]
