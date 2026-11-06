
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)
from .models import MMCTestimonial

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

    # -----------------------------------------
    # Existing Volunteer Opportunity Data
    # -----------------------------------------
    featured_opportunity = VolunteerOpportunity.objects.filter(
        is_open=True
    ).exclude(
        slug=""
    ).order_by("ordering", "title").first()

    # -----------------------------------------
    # Career Board Statistics
    # -----------------------------------------
    career_queryset = JobVacancy.objects.all()

    inactive_statuses = ["closed", "cancelled", "filled"]

    active_careers = career_queryset.exclude(
        status__in=inactive_statuses
    )

    total_open_count = active_careers.count()

    volunteer_count = active_careers.filter(
        employment_type="volunteer"
    ).count()

    internship_count = active_careers.filter(
        employment_type="internships"
    ).count()

    staff_count = active_careers.filter(
        employment_type="jobs"
    ).count()

    consultant_count = active_careers.filter(
        employment_type="consulting"
    ).count()

    # -----------------------------------------
    # Four Career Board Filters
    # -----------------------------------------
    selected_type = request.GET.get("type", "").strip()
    selected_location = request.GET.get("location", "").strip()
    selected_functional_area = request.GET.get(
        "functional_area", ""
    ).strip()
    selected_status = request.GET.get("status", "").strip()

    vacancies = career_queryset

    if selected_type:
        vacancies = vacancies.filter(
            employment_type=selected_type
        )

    if selected_location:
        vacancies = vacancies.filter(
            location=selected_location
        )

    if selected_functional_area:
        vacancies = vacancies.filter(
            functional_area=selected_functional_area
        )

    if selected_status:
        vacancies = vacancies.filter(
            status=selected_status
        )

    vacancies = vacancies.order_by(
        "ordering",
        "title"
    )

    # -----------------------------------------
    # Voices of MMC Testimonials
    # -----------------------------------------
    testimonials = MMCTestimonial.objects.filter(
        is_active=True
    ).order_by(
        "ordering",
        "-created_at"
    )

    # -----------------------------------------
    # Page Context
    # -----------------------------------------
    context = {
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": "volunteer",

        # Existing featured opportunity
        "featured_opportunity": featured_opportunity,

        # Career Board data
        "vacancies": vacancies,

        # Career Board counters
        "total_open_count": total_open_count,
        "volunteer_count": volunteer_count,
        "internship_count": internship_count,
        "staff_count": staff_count,
        "consultant_count": consultant_count,

        # Filter choices
        "type_choices": JobVacancy.TYPE_CHOICES,
        "location_choices": JobVacancy.LOCATION_CHOICES,
        "functional_area_choices": JobVacancy.FUNCTIONAL_AREA_CHOICES,
        "status_choices": JobVacancy.STATUS_CHOICES,

        # Selected filters
        "selected_type": selected_type,
        "selected_location": selected_location,
        "selected_functional_area": selected_functional_area,
        "selected_status": selected_status,

        # Voices of MMC
        "testimonials": testimonials,
    }

    return render(
        request,
        "engagement/volunteer_opportunities.html",
        context
    )




def job_vacancies(request):
    vacancies = JobVacancy.objects.all()

    # Type filter
    selected_type = request.GET.get("type", "").strip()
    if selected_type:
        vacancies = vacancies.filter(
            employment_type=selected_type
        )

    # Location filter
    selected_location = request.GET.get("location", "").strip()
    if selected_location:
        vacancies = vacancies.filter(
            location=selected_location
        )

    # Functional Area filter
    selected_functional_area = request.GET.get(
        "functional_area", ""
    ).strip()

    if selected_functional_area:
        vacancies = vacancies.filter(
            functional_area=selected_functional_area
        )

    # Status filter
    selected_status = request.GET.get("status", "").strip()
    if selected_status:
        vacancies = vacancies.filter(
            status=selected_status
        )

    vacancies = vacancies.order_by(
        "ordering",
        "title",
    )

    context = {
        "vacancies": vacancies,
        "get_involved_menu": GET_INVOLVED_MENU,

        "type_choices": JobVacancy.TYPE_CHOICES,
        "location_choices": JobVacancy.LOCATION_CHOICES,
        "functional_area_choices": JobVacancy.FUNCTIONAL_AREA_CHOICES,
        "status_choices": JobVacancy.STATUS_CHOICES,

        "selected_type": selected_type,
        "selected_location": selected_location,
        "selected_functional_area": selected_functional_area,
        "selected_status": selected_status,
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



def job_vacancy_detail(request, slug):
    vacancy = get_object_or_404(
        JobVacancy,
        slug=slug
    )

    context = {
        "vacancy": vacancy,
        "get_involved_menu": GET_INVOLVED_MENU,
        "active_engagement_slug": "volunteer",
    }

    return render(
        request,
        "engagement/job_vacancy_detail.html",
        context
    )

