from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.projects import views

# Partials Requests
urlpatterns = [
    url(r'^partials/list/', views.ProjectList.get_partial, name='projects-list-partial'),
]

# API Requests
urlpatterns += format_suffix_patterns([
    url(r'^$', views.ProjectList.as_view(), name='projects-list'),
])