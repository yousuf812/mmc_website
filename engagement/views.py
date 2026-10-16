
from django.shortcuts import get_object_or_404, render

from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)


# Shared submenu for all Get Involved pages
GET_INVOLVED_MENU = [
    {
        "title": "Volunteer",
        "slug": "volunteer",
    },
    {
        "title": "Careers",
        "slug": "careers",
    },
    {
        "title": "Partnerships",
        "slug": "partnerships",
    },
    {
        "title": "Donate & Support",
        "slug": "donate-support",
    },
    {
        "title": "Clients",
        "slug": "customers-clients",
    },
    {
        "title": "Suppliers & Contractors",
        "slug": "suppliers-contractors",
    },
]


def get_involved_home(request):
    pages = EngagementPage.objects.filter(
        is_published=True
    ).order_by("ordering", "title")

    opportunities = VolunteerOpportunity.objects.filter(
        is_open=True
    ).order_by("ordering", "title")[:3]

    vacancies = JobVacancy.objects.filter(
        is_open=True
    ).order_by("ordering", "title")[:3]

    context = {
        "pages": pages,
        "opportunities": opportunities,
        "vacancies": vacancies,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": "",
    }

    return render(
        request,
        "engagement/get_involved_home.html",
        context,
    )


def engagement_page(request, slug):
    page = get_object_or_404(
        EngagementPage,
        slug=slug,
        is_published=True,
    )

    context = {
        "page": page,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": page.slug,
    }

    return render(
        request,
        "engagement/engagement_page.html",
        context,
    )


def volunteer_opportunities(request):
    opportunities = VolunteerOpportunity.objects.filter(
        is_open=True
    ).order_by("ordering", "title")

    context = {
        "opportunities": opportunities,
        "get_involved_menu": GET_INVOLVED_MENU,
    }

    return render(
        request,
        "engagement/volunteer_opportunities.html",
        context,
    )


def job_vacancies(request):
    vacancies = JobVacancy.objects.filter(
        is_open=True
    ).order_by("ordering", "title")

    context = {
        "vacancies": vacancies,
        "get_involved_menu": GET_INVOLVED_MENU,
    }

    return render(
        request,
        "engagement/job_vacancies.html",
        context,
    )
