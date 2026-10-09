from django.shortcuts import render
from projects.models import Project
from news.models import NewsArticle
from team.models import TeamMember

from .models import (
    AboutPage,
    JourneyMilestone,
    GovernanceOverview,
)

from pages.models import (
    Homepage,
    SiteSettings,
    StrategicPriority,
    ImpactStatistic,
)

def home(request):
    site_settings = SiteSettings.objects.filter(
        is_active=True
    ).first()

    homepage = Homepage.objects.filter(
        is_active=True
    ).first()

    priorities = StrategicPriority.objects.filter(
        is_active=True
    ).order_by("ordering", "number")

    statistics = ImpactStatistic.objects.filter(
        is_active=True
    ).order_by("ordering")

    featured_projects = (
        Project.objects
        .filter(
            is_published=True,
            is_featured=True,
            project_status__in=["planned", "active", "completed"],
        )
        .select_related("priority")
        .prefetch_related("sectors")
        .order_by("ordering", "title")[:3]
    )

    latest_articles = (
        NewsArticle.objects
        .filter(is_published=True)
        .order_by("-is_featured", "-published_at", "ordering")[:3]
    )

    context = {
        "site_settings": site_settings,
        "homepage": homepage,
        "priorities": priorities,
        "statistics": statistics,
        "featured_projects": featured_projects,
        "latest_articles": latest_articles,
    }

    return render(request, "home.html", context)



def about(request):
    about_page = (
        AboutPage.objects
        .filter(is_published=True)
        .first()
    )

    milestones = (
        JourneyMilestone.objects
        .filter(is_published=True)
        .order_by("year", "ordering")
    )

    governance = (
        GovernanceOverview.objects
        .filter(is_published=True)
        .first()
    )

    team_members = (
        TeamMember.objects
        .filter(is_active=True)
        .order_by("category", "ordering", "name")
    )

    context = {
        "about_page": about_page,
        "milestones": milestones,
        "governance": governance,
        "team_members": team_members,
    }

    return render(
        request,
        "pages/about.html",
        context
    )