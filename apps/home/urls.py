from django.conf.urls import include, url
from django.contrib import admin
import apps.home.views

urlpatterns = [
    url(r'^$', apps.home.views.index, name='home-index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('apps.blog.urls')),
    url(r'^projects/', include('apps.projects.urls')),
]
