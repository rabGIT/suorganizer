from django.conf.urls import url

from ..views import (
    StartupCreate, StartupDelete, StartupUpdate,
    startup_detail, startup_list)

urlpatterns = [
    url(r'^$',
        startup_list,
        name='organizer_startup_list'),
    url(r'^create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    url(r'^(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    url(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
]
