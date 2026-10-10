from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
     path("contact/",include("contact.urls")),
     path("", include("pages.urls")),
     path("", include("projects.urls")),
     path("resources/news/", include("news.urls")),
     path("resources/",include("resources.urls")),
     path("get-involved/",include("engagement.urls")),
     path("tenders/", include("tenders.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )