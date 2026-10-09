from django.shortcuts import get_object_or_404, render

from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)


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

    return render(
        request,
        "engagement/engagement_page.html",
        {"page": page},
    )


def volunteer_opportunities(request):
    opportunities = VolunteerOpportunity.objects.filter(
        is_open=True
    ).order_by("ordering", "title")

    return render(
        request,
        "engagement/volunteer_opportunities.html",
        {"opportunities": opportunities},
    )


def job_vacancies(request):
    vacancies = JobVacancy.objects.filter(
        is_open=True
    ).order_by("ordering", "title")

    return render(
        request,
        "engagement/job_vacancies.html",
        {"vacancies": vacancies},
    )