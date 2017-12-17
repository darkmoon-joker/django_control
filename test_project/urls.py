from django.contrib import admin

try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import include, url
else:
    def include(urls):
        return urls  # compatibility mock for dj > 2.0

from controlcenter.views import controlcenter


urlpatterns = [
    url(r'admin/dashboard/', include(controlcenter.urls)),
    url(r'admin/', include(admin.site.urls)),
]
