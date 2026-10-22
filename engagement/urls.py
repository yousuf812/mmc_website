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

    path(
    "job-vacancies/<slug:slug>/apply/",
    views.job_application,
    name="job_application",
),


path(
    "volunteer-opportunities/<slug:slug>/apply/",
    views.volunteer_application,
    name="volunteer_application",
),

]