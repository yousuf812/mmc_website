from django.contrib import admin

from .models import (
    DeliveryEngine,
    Project,
    ProjectPriority,
    ProjectSector,
    SDG,
    PriorityAction,
    WhatWeDoPage,
    CrossCuttingCommitment,
)


@admin.register(ProjectPriority)
class ProjectPriorityAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering = [
        "ordering",
        "name",
    ]


@admin.register(ProjectSector)
class ProjectSectorAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering = [
        "ordering",
        "name",
    ]


@admin.register(SDG)
class SDGAdmin(admin.ModelAdmin):

    list_display = [
        "number",
        "title",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "title",
        "description",
    ]

    ordering = [
        "number",
    ]


@admin.register(DeliveryEngine)
class DeliveryEngineAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering = [
        "ordering",
        "name",
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "priority",
        "client_donor",
        "location",
        "project_status",
        "is_featured",
        "is_published",
    ]

    list_filter = [
        "priority",
        "project_status",
        "is_featured",
        "is_published",
        "sectors",
        "sdgs",
        "delivery_engines",
    ]

    search_fields = [
        "title",
        "project_code",
        "short_description",
        "description",
        "location",
        "country",
        "client_donor",
        "outcomes",
        "impact_summary",
    ]

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = [
        "sectors",
        "sdgs",
        "delivery_engines",
    ]

    date_hierarchy = "start_date"

    ordering = [
        "-is_featured",
        "ordering",
        "-start_date",
        "title",
    ]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "project_code",
                    "short_description",
                    "description",
                    "featured_image",
                    "image_alt_text",
                )
            },
        ),
        (
            "Classification & Filtering",
            {
                "fields": (
                    "priority",
                    "sectors",
                    "sdgs",
                    "delivery_engines",
                )
            },
        ),
        (
            "Project Details",
            {
                "fields": (
                    "location",
                    "country",
                    "client_donor",
                    "start_date",
                    "end_date",
                    "project_status",
                )
            },
        ),
        (
            "Impact & Learning",
            {
                "fields": (
                    "outcomes",
                    "impact_summary",
                    "beneficiaries",
                    "success_story",
                    "testimonial",
                    "testimonial_name",
                    "testimonial_role",
                    "video_url",
                )
            },
        ),
        (
            "Reports",
            {
                "fields": (
                    "baseline_report",
                    "final_report",
                    "endline_report",
                )
            },
        ),
        (
            "Predecessor & Publishing",
            {
                "fields": (
                    "predecessor_note",
                    "is_featured",
                    "is_published",
                    "ordering",
                )
            },
        ),
    )



@admin.register(WhatWeDoPage)
class WhatWeDoPageAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "is_published",
        "updated_at",
    ]

    list_filter = [
        "is_published",
    ]

    search_fields = [
        "title",
        "subtitle",
        "why_mmc_content",
        "model_description",
    ]

    fieldsets = (
        (
            "Page Header",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "is_published",
                )
            },
        ),
        (
            "Why MMC Exists",
            {
                "fields": (
                    "why_mmc_title",
                    "why_mmc_content",
                )
            },
        ),
        (
            "MMC Model of Change",
            {
                "fields": (
                    "model_title",
                    "model_description",
                )
            },
        ),
        (
            "Strategic Priorities",
            {
                "fields": (
                    "priorities_intro",
                )
            },
        ),
        (
            "Delivery Engines",
            {
                "fields": (
                    "delivery_intro",
                )
            },
        ),
        (
            "Cross-Cutting Commitments",
            {
                "fields": (
                    "commitments_title",
                    "commitments_intro",
                )
            },
        ),
    )


@admin.register(PriorityAction)
class PriorityActionAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "priority",
        "ordering",
        "is_published",
    ]

    list_filter = [
        "priority",
        "is_published",
    ]

    search_fields = [
        "title",
        "description",
        "priority__title",
    ]

    ordering = [
        "priority",
        "ordering",
        "title",
    ]

    fieldsets = (
        (
            "Priority Action",
            {
                "fields": (
                    "priority",
                    "title",
                    "description",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "ordering",
                    "is_published",
                )
            },
        ),
    )


@admin.register(CrossCuttingCommitment)
class CrossCuttingCommitmentAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "ordering",
        "is_published",
    ]

    list_filter = [
        "is_published",
    ]

    search_fields = [
        "title",
        "standard",
    ]

    ordering = [
        "ordering",
        "title",
    ]

    fieldsets = (
        (
            "Commitment",
            {
                "fields": (
                    "title",
                    "standard",
                    "icon",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "ordering",
                    "is_published",
                )
            },
        ),
    )