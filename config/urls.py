from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),

    path("contact/", include("contact.urls")),

    path("", include("pages.urls")),
    path("", include("projects.urls")),

    path("resources/news/", include("news.urls")),
    path("resources/", include("resources.urls")),

    path("get-involved/", include("engagement.urls")),

    # Main Buyer URL
    path("supply-for-us/", include("tenders.urls")),

    # Old URL Redirect
    path(
        "tenders/",
        RedirectView.as_view(
            url="/supply-for-us/",
            permanent=True
        ),
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )