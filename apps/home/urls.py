from django.conf.urls import url
import apps.home.views

urlpatterns = [
    url(r'^$', apps.home.views.index, name='home-index'),
]
