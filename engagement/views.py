
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)

from django.contrib import messages
from django.shortcuts import redirect

from .forms import JobApplicationForm
from .models import VolunteerApplication
from .forms import VolunteerApplicationForm


# Shared submenu for all Get Involved pages

# Shared submenu for all Get Involved pages
GET_INVOLVED_MENU = [
    {
        "title": "Work with us",
        "slug": "join-our-team",
    },
    {
        "title": "Fund us",
        "slug": "donors",
    },
    {
        "title": "Supply for us",
        "slug": "suppliers-contractors",
    },
    {
        "title": "Partner with us",
        "slug": "partnerships",
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

    # Join Our Team combines the existing Volunteer
    # and Careers page content.
    if slug == "join-our-team":
        volunteer_page = get_object_or_404(
            EngagementPage,
            slug="volunteer",
            is_published=True,
        )

        careers_page = get_object_or_404(
            EngagementPage,
            slug="careers",
            is_published=True,
        )

        return render(
            request,
            "engagement/join_our_team.html",
            {
                "volunteer_page": volunteer_page,
                "careers_page": careers_page,
                "get_involved_menu": GET_INVOLVED_MENU,
                "active_engagement_slug": "join-our-team",
            },
        )

    # Donors uses the existing Donate & Support page content.
    page_slug = (
        "donate-support"
        if slug in ("donors", "only-donors")
        else slug
    )

    page = get_object_or_404(
        EngagementPage,
        slug=page_slug,
        is_published=True,
    )

    page_templates = {
        "partnerships": "engagement/partnerships.html",
        "donate-support": "engagement/donate_support.html",
        "customers-clients": "engagement/clients.html",
    }

    template_name = page_templates.get(
        page.slug,
        "engagement/engagement_page.html",
    )

    context = {
        "page": page,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": slug,
    }

    return render(
        request,
        template_name,
        context,
    )



def volunteer_opportunities(request):
    queryset = VolunteerOpportunity.objects.all()

    # Stat counters (Image onujayi)
    total_open_count = queryset.filter(is_open=True).count()
    volunteer_count = queryset.filter(is_open=True, opportunity_type="volunteer").count()
    internship_count = queryset.filter(is_open=True, opportunity_type="internship").count()
    staff_count = queryset.filter(is_open=True, opportunity_type="staff").count()

    # Distinct values for dropdown filters
    areas_list = (
        VolunteerOpportunity.objects.exclude(area__exact="")
        .values_list("area", flat=True)
        .distinct()
    )
    locations_list = (
        VolunteerOpportunity.objects.exclude(location__exact="")
        .values_list("location", flat=True)
        .distinct()
    )

    # Filter parameters from GET request
    q = request.GET.get("q", "").strip()
    opp_type = request.GET.get("type", "").strip()
    area = request.GET.get("area", "").strip()
    location = request.GET.get("location", "").strip()
    status = request.GET.get("status", "").strip()

    # Apply Filters
    if q:
        queryset = queryset.filter(
            Q(title__icontains=q)
            | Q(area__icontains=q)
            | Q(location__icontains=q)
            | Q(description__icontains=q)
        )
    if opp_type:
        queryset = queryset.filter(opportunity_type=opp_type)
    if area:
        queryset = queryset.filter(area=area)
    if location:
        queryset = queryset.filter(location=location)
    if status == "open":
        queryset = queryset.filter(is_open=True)
    elif status == "closed":
        queryset = queryset.filter(is_open=False)

    opportunities = queryset.order_by("ordering", "title")
    featured_opportunity = VolunteerOpportunity.objects.filter(
        is_open=True
    ).exclude(
        slug=""
    ).order_by("ordering", "title").first()

    context = {
        "opportunities": opportunities,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": "volunteer",
        "featured_opportunity": featured_opportunity,
        # Counters
        "total_open_count": total_open_count,
        "volunteer_count": volunteer_count,
        "internship_count": internship_count,
        "staff_count": staff_count,
        # Filter options
        "areas_list": areas_list,
        "locations_list": locations_list,
        # Selected filter states
        "selected_q": q,
        "selected_type": opp_type,
        "selected_area": area,
        "selected_location": location,
        "selected_status": status,
    }

    return render(
        request, 
        "engagement/volunteer_opportunities.html", 
        context
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




def volunteer_application(request, slug):
    opportunity = get_object_or_404(
        VolunteerOpportunity,
        slug=slug,
        is_open=True,
    )

    # Staff / Career applications use the Job Application form.
    if opportunity.opportunity_type == "staff":
        vacancy = JobVacancy.objects.filter(
            slug=slug,
            is_open=True,
        ).first()

        if vacancy is None:
            messages.error(
                request,
                "This career opportunity is not linked to a Job Vacancy record yet. Please add the vacancy in Admin.",
            )
            return redirect("engagement:job_vacancies")

        return redirect(
            "engagement:job_application",
            slug=vacancy.slug,
        )

    # Check the deadline for volunteer, internship, and consultant.
    if opportunity.deadline:
        from django.utils import timezone

        if opportunity.deadline < timezone.localdate():
            messages.error(
                request,
                "The application deadline for this opportunity has passed.",
            )
            return redirect("engagement:volunteer_opportunities")

    # Process the volunteer application form.
    if request.method == "POST":
        form = VolunteerApplicationForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            application = form.save(commit=False)
            application.opportunity = opportunity
            application.save()

            messages.success(
                request,
                "Your application has been submitted successfully.",
            )

            return redirect("engagement:volunteer_opportunities")

    else:
        form = VolunteerApplicationForm()

    return render(
        request,
        "engagement/volunteer_application_form.html",
        {
            "opportunity": opportunity,
            "form": form,
            "get_involved_menu": GET_INVOLVED_MENU,
            "active_engagement_slug": "join-our-team",
        },
    )

