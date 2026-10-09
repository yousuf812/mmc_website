from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "title",
        "category",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "category",
        "is_active",
    ]

    search_fields = [
        "name",
        "title",
        "academic_qualification",
        "technical_background",
        "mandate",
    ]

    ordering = [
        "category",
        "ordering",
        "name",
    ]

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "name",
                    "title",
                    "category",
                    "photograph",
                    "accessibility_alt_text",
                )
            },
        ),
        (
            "Professional Information",
            {
                "fields": (
                    "academic_qualification",
                    "technical_background",
                    "mandate",
                    "biography",
                    "linkedin_url",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "ordering",
                    "is_active",
                )
            },
        ),
    )