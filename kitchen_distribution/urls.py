from django.contrib import admin
from django.urls import path, include

import catalog


urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("", catalog.views.index, name="index"),
]

app_name = "admin"
