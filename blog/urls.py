from django.conf.urls import url

from .views import post_detail, PostList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    url(r'^$', PostList.as_view(), name='blog_post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$', PostUpdate.as_view(),
        name='blog_post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$', PostDelete.as_view(),
        name='blog_post_delete'),
    url(r'^create/$', PostCreate.as_view(), name='blog_post_create')
]
