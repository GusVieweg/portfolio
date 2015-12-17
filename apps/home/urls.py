from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'apps.home.views.index', name='home-index'),
    url(r'^sample/', include('apps.sample.urls')),
]
