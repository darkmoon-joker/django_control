from django.conf.urls import include, url
from django.contrib import admin

from controlcenter.views import controlcenter

urlpatterns = [
    url(r'^admin/dashboard/', include(controlcenter.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
