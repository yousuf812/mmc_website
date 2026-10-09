from django.urls import path

from . import views


app_name = "resources"


urlpatterns = [
    path(
        "publications/",
        views.publication_list,
        name="publication_list",
    ),

    path(
        "publications/<slug:slug>/",
        views.publication_detail,
        name="publication_detail",
    ),

    path(
        "gallery/",
        views.gallery_list,
        name="gallery",
    ),

    path(
        "press-kit/",
        views.press_kit,
        name="press_kit",
    ),
]