from django.contrib import admin
from django.urls import path
from .api.v1 import api as api_v1
from .api.v2 import api as api_v2

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', api_v1.urls),
    path('api/v2/', api_v2.urls),
]
