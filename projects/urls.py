
from django.urls import path

from . import views


app_name = "projects"


urlpatterns = [
    path(
        "what-we-do/",
        views.what_we_do,
        name="what_we_do",
    ),

    # Our Work: Our Projects
    path(
        "projects/",
        views.project_list,
        name="project_list",
    ),

    path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),

    # Our Work: Our Impact
    path(
        "our-impact/",
        views.our_impact,
        name="our_impact",
    ),
]
