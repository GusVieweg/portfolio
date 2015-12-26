from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.research import views

# Partials Requests
urlpatterns = [
    url(r'^([0-9]+)/$', views.research_post),
    url(r'^partials/list/', views.get_partial, name='research-list-partial'),
]

# API Requests
urlpatterns += format_suffix_patterns([
    url(r'^$', views.ResearchList.as_view(), name='research-list'),
])