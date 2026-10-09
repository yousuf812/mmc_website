from django.urls import path

from . import views


app_name = "engagement"


urlpatterns = [
    path(
        "",
        views.get_involved_home,
        name="home",
    ),

    path(
        "volunteer-opportunities/",
        views.volunteer_opportunities,
        name="volunteer_opportunities",
    ),

    path(
        "job-vacancies/",
        views.job_vacancies,
        name="job_vacancies",
    ),

    path(
        "<slug:slug>/",
        views.engagement_page,
        name="page",
    ),
]