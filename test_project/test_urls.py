# to reload urls in tests

from urls import *  # NOQA

urlpatterns = [
    url(r'^admin/dashboard/', include(controlcenter.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
