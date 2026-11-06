
from django.urls import path

from . import views
from django.views.generic import RedirectView


app_name = "engagement"


urlpatterns = [
    # Get Involved landing page
    path(
        "",
        views.get_involved_home,
        name="home",
    ),

    # Volunteer opportunities
   path(
    "work-for-us/",
    views.volunteer_opportunities,
    name="volunteer_opportunities"
),

path(
    "volunteer-opportunities/",
    RedirectView.as_view(
        pattern_name="engagement:volunteer_opportunities",
        permanent=True
    ),
),

    # Volunteer application
    path(
        "volunteer-opportunities/<slug:slug>/apply/",
        views.volunteer_application,
        name="volunteer_application",
    ),

    # Job vacancies
    path(
        "job-vacancies/",
        views.job_vacancies,
        name="job_vacancies",
    ),

    # Job application
    path(
        "job-vacancies/<slug:slug>/apply/",
        views.job_application,
        name="job_application",
    ),

    # Individual engagement pages
    path(
        "<slug:slug>/",
        views.engagement_page,
        name="page",
    ),

     path(
        "job-vacancies/<slug:slug>/",
        views.job_vacancy_detail,
        name="job_vacancy_detail",
    ),
]
