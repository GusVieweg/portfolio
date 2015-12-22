from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.blog import views

# Partials Requests
urlpatterns = [
    url(r'^([0-9]+)/$', views.blog_post),
    url(r'^partials/list/', views.get_partial, name='blog-list-partial'),
]

# API Requests
urlpatterns += format_suffix_patterns([
    url(r'^$', views.PostList.as_view(), name='blog-list'),
])
