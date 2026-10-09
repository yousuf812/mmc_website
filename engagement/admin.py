from django.contrib import admin

from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
)


@admin.register(EngagementPage)
class EngagementPageAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "page_type",
        "is_published",
        "ordering",
        "updated_at",
    ]

    list_filter = [
        "page_type",
        "is_published",
    ]

    search_fields = [
        "title",
        "short_description",
        "content",
        "why_engage",
    ]

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = [
        "ordering",
        "title",
    ]

    fieldsets = (
        (
            "Page Information",
            {
                "fields": (
                    "page_type",
                    "title",
                    "slug",
                    "short_description",
                    "content",
                )
            },
        ),
        (
            "Engagement Details",
            {
                "fields": (
                    "why_engage",
                    "process",
                    "requirements",
                )
            },
        ),
        (
            "Call To Action",
            {
                "fields": (
                    "call_to_action",
                    "call_to_action_url",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "featured_image",
                    "image_alt_text",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                    "ordering",
                )
            },
        ),
    )


@admin.register(VolunteerOpportunity)
class VolunteerOpportunityAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "location",
        "deadline",
        "is_open",
        "ordering",
    ]

    list_filter = [
        "is_open",
        "location",
        "deadline",
    ]

    search_fields = [
        "title",
        "description",
        "location",
        "requirements",
    ]

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = [
        "ordering",
        "title",
    ]

    fieldsets = (
        (
            "Opportunity Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "location",
                    "description",
                )
            },
        ),
        (
            "Role Details",
            {
                "fields": (
                    "responsibilities",
                    "requirements",
                )
            },
        ),
        (
            "Application",
            {
                "fields": (
                    "application_instructions",
                    "application_email",
                    "application_url",
                    "deadline",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_open",
                    "ordering",
                )
            },
        ),
    )


@admin.register(JobVacancy)
class JobVacancyAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "department",
        "location",
        "employment_type",
        "closing_date",
        "is_open",
        "ordering",
    ]

    list_filter = [
        "is_open",
        "department",
        "location",
        "employment_type",
        "closing_date",
    ]

    search_fields = [
        "title",
        "department",
        "location",
        "description",
        "qualifications",
        "experience",
    ]

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = [
        "ordering",
        "-created_at",
    ]

    fieldsets = (
        (
            "Vacancy Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "department",
                    "location",
                    "employment_type",
                )
            },
        ),
        (
            "Job Details",
            {
                "fields": (
                    "description",
                    "responsibilities",
                    "qualifications",
                    "experience",
                )
            },
        ),
        (
            "Application",
            {
                "fields": (
                    "application_instructions",
                    "application_email",
                    "application_url",
                    "closing_date",
                )
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_open",
                    "ordering",
                )
            },
        ),
    )