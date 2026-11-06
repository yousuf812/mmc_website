
from django.shortcuts import get_object_or_404, render

from pages.models import StrategicPriority
from pages.models import ImpactStatistic
from django.db.models import Q

from .models import (
    WhatWeDoPage,
    DeliveryEngine,
    CrossCuttingCommitment,
    Project,
    ProjectSector,
    SDG,
    ImpactMetric,
)


def what_we_do(request):
    page = (
        WhatWeDoPage.objects
        .filter(is_published=True)
        .first()
    )

    priorities = (
        StrategicPriority.objects
        .filter(is_active=True)
        .prefetch_related("actions")
        .order_by("ordering", "number")
    )

    delivery_engines = (
        DeliveryEngine.objects
        .filter(is_active=True)
        .order_by("ordering", "name")
    )

    commitments = (
        CrossCuttingCommitment.objects
        .filter(is_published=True)
        .order_by("ordering", "title")
    )

    context = {
        "page": page,
        "priorities": priorities,
        "delivery_engines": delivery_engines,
        "commitments": commitments,
    }

    return render(
        request,
        "projects/what_we_do.html",
        context,
    )


def project_list(request):
    projects = (
        Project.objects
        .filter(
            is_published=True,
            project_status__in=["planned", "active", "completed"],
        )
        .select_related("priority")
        .prefetch_related(
            "sectors",
            "sdgs",
            "delivery_engines",
        )
        .order_by(
            "-is_featured",
            "ordering",
            "-start_date",
            "title",
        )
    )

    # Search
    search_query = request.GET.get("q", "").strip()

    if search_query:
        projects = (
            projects.filter(title__icontains=search_query)
            | projects.filter(
                short_description__icontains=search_query
            )
            | projects.filter(location__icontains=search_query)
            | projects.filter(client_donor__icontains=search_query)
        )

    # Strategic Priority
    priority_id = request.GET.get("priority", "").strip()

    if priority_id.isdigit():
        projects = projects.filter(priority_id=priority_id)

    # Sector
    sector_id = request.GET.get("sector", "").strip()

    if sector_id.isdigit():
        projects = projects.filter(sectors__id=sector_id)

    # SDG
    sdg_id = request.GET.get("sdg", "").strip()

    if sdg_id.isdigit():
        projects = projects.filter(sdgs__id=sdg_id)

    # Delivery Engine
    delivery_engine_id = request.GET.get(
        "delivery_engine",
        "",
    ).strip()

    if delivery_engine_id.isdigit():
        projects = projects.filter(
            delivery_engines__id=delivery_engine_id
        )

    # Project Status
    status = request.GET.get("status", "").strip()

    allowed_statuses = {
        "planned",
        "active",
        "completed",
    }

    if status in allowed_statuses:
        projects = projects.filter(project_status=status)

    # Filter options
    priorities = (
        StrategicPriority.objects
        .filter(is_active=True)
        .order_by("ordering", "number")
    )

    sectors = (
        ProjectSector.objects
        .filter(is_active=True)
        .order_by("ordering", "name")
    )

    sdgs = (
        SDG.objects
        .filter(is_active=True)
        .order_by("ordering", "number")
    )

    delivery_engines = (
        DeliveryEngine.objects
        .filter(is_active=True)
        .order_by("ordering", "name")
    )

    
    statistics = ImpactStatistic.objects.filter(
        is_active=True
    ).order_by("ordering")

    context = {
        "projects": projects.distinct(),
        "priorities": priorities,
        "sectors": sectors,
        "sdgs": sdgs,
        "delivery_engines": delivery_engines,
        "statistics": statistics,
        "search_query": search_query,
        "selected_priority": priority_id,
        "selected_sector": sector_id,
        "selected_sdg": sdg_id,
        "selected_delivery_engine": delivery_engine_id,
        "selected_status": status,
        "active_work_section": "projects",
    }

    return render(
        request,
        "projects/project_list.html",
        context,
    )



def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects
        .select_related("priority")
        .prefetch_related(
            "sectors",
            "sdgs",
            "delivery_engines",
        ),
        slug=slug,
        is_published=True,
    )

    context = {
        "project": project,
        "active_work_section": "projects",
    }

    return render(
        request,
        "projects/project_detail.html",
        context,
    )




def our_impact(request):
    completed_projects = (
        Project.objects
        .filter(
            is_published=True,
            project_status="completed",
        )
        .select_related("priority")
        .prefetch_related(
            "sectors",
            "sdgs",
            "delivery_engines",
        )
    )

    # Keyword Search
    search_query = request.GET.get("q", "").strip()

    if search_query:
        completed_projects = completed_projects.filter(
            Q(title__icontains=search_query)
            | Q(short_description__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(location__icontains=search_query)
            | Q(client_donor__icontains=search_query)
            | Q(impact_summary__icontains=search_query)
            | Q(success_story__icontains=search_query)
        )

    # Location Filter
    location = request.GET.get("location", "").strip()

    if location:
        completed_projects = completed_projects.filter(
            location__icontains=location
        )

    # Sector Filter
    sector_id = request.GET.get("sector", "").strip()

    if sector_id.isdigit():
        completed_projects = completed_projects.filter(
            sectors__id=sector_id
        )

    completed_projects = completed_projects.order_by(
        "-is_featured",
        "ordering",
        "-start_date",
        "title",
    ).distinct()

    # Active Sector Options
    sectors = (
        ProjectSector.objects
        .filter(is_active=True)
        .order_by("ordering", "name")
    )

    # Published Impact Metrics
    impact_metrics = (
        ImpactMetric.objects
        .filter(is_published=True)
        .order_by("ordering", "title")
    )

    # Published Success Stories
    success_stories = (
        Project.objects
        .filter(
            is_published=True,
            project_status="completed",
        )
        .exclude(success_story="")
        .select_related("priority")
        .order_by(
            "-is_featured",
            "ordering",
            "-start_date",
            "title",
        )
    )

    # Published Testimonials
    testimonials = (
        Project.objects
        .filter(
            is_published=True,
            testimonial__gt="",
        )
        .select_related("priority")
        .order_by(
            "-is_featured",
            "ordering",
            "-start_date",
            "title",
        )
    )

    context = {
        "active_work_section": "impact",
        "completed_projects": completed_projects,
        "completed_projects_count": completed_projects.count(),
        "impact_metrics": impact_metrics,
        "success_stories": success_stories,
        "testimonials": testimonials,
        "sectors": sectors,
        "search_query": search_query,
        "selected_sector": sector_id,
        "location_query": location,
    }

    return render(
        request,
        "projects/our_impact.html",
        context,
    )
