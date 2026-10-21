
from django.shortcuts import get_object_or_404, render

from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)

from django.contrib import messages
from django.shortcuts import redirect

from .forms import JobApplicationForm


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

    # Dedicated frontend templates for selected pages
    page_templates = {
        "partnerships": "engagement/partnerships.html",
        "donate-support": "engagement/donate_support.html",
        "customers-clients": "engagement/clients.html",
    }

    # Keep the existing template for Volunteer, Careers,
    # Suppliers & Contractors, and other engagement pages.
    template_name = page_templates.get(
        page.slug,
        "engagement/engagement_page.html",
    )

    context = {
        "page": page,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": page.slug,
    }

    return render(
        request,
        template_name,
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
    )

    search_query = request.GET.get("q", "").strip()

    if search_query:
        from django.db.models import Q

        vacancies = vacancies.filter(
            Q(title__icontains=search_query)
            | Q(department__icontains=search_query)
            | Q(location__icontains=search_query)
            | Q(employment_type__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(qualifications__icontains=search_query)
            | Q(experience__icontains=search_query)
        )

    vacancies = vacancies.order_by(
        "ordering",
        "title",
    )

    context = {
        "vacancies": vacancies,
        "get_involved_menu": GET_INVOLVED_MENU,
        "search_query": search_query,
    }

    return render(
        request,
        "engagement/job_vacancies.html",
        context,
    )



def job_application(request, slug):
    vacancy = get_object_or_404(
        JobVacancy,
        slug=slug,
        is_open=True,
    )

    if vacancy.closing_date:
        from django.utils import timezone

        if vacancy.closing_date < timezone.localdate():
            messages.error(
                request,
                "The application deadline for this vacancy has passed.",
            )
            return redirect("engagement:job_vacancies")

    if request.method == "POST":
        form = JobApplicationForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.save()

            messages.success(
                request,
                "Your application has been submitted successfully.",
            )

            return redirect("engagement:job_vacancies")

    else:
        form = JobApplicationForm()

    return render(
        request,
        "engagement/job_application_form.html",
        {
            "vacancy": vacancy,
            "form": form,
            "get_involved_menu": GET_INVOLVED_MENU,
        },
    )

