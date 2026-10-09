from django.contrib import admin

from .models import (
    Homepage,
    ImpactStatistic,
    SiteSettings,
    StrategicPriority,
    AboutPage,
    JourneyMilestone,
    GovernanceOverview,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = [
        "site_name",
        "email",
        "phone_1",
        "is_active",
        "updated_at",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "site_name",
        "email",
        "address",
    ]


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):

    list_display = [
        "hero_title",
        "is_active",
        "updated_at",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "hero_title",
        "hero_description",
        "mission_text",
        "vision_text",
    ]


@admin.register(StrategicPriority)
class StrategicPriorityAdmin(admin.ModelAdmin):

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
        "short_description",
        "full_description",
    ]

    ordering = [
        "ordering",
        "number",
    ]


@admin.register(ImpactStatistic)
class ImpactStatisticAdmin(admin.ModelAdmin):

    list_display = [
        "value",
        "label",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "is_active",
    ]

    search_fields = [
        "value",
        "label",
        "description",
    ]

    ordering = [
        "ordering",
    ]



@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):

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
        "about_content",
        "purpose_content",
        "mission_content",
        "vision_content",
    ]

    fieldsets = (
        (
            "Page Header",
            {
                "fields": (
                    "title",
                    "subtitle",
                    "featured_image",
                    "image_alt_text",
                    "is_published",
                )
            },
        ),
        (
            "About MMC",
            {
                "fields": (
                    "about_title",
                    "about_content",
                )
            },
        ),
        (
            "Purpose",
            {
                "fields": (
                    "purpose_title",
                    "purpose_content",
                )
            },
        ),
        (
            "Mission",
            {
                "fields": (
                    "mission_title",
                    "mission_content",
                )
            },
        ),
        (
            "Vision",
            {
                "fields": (
                    "vision_title",
                    "vision_content",
                )
            },
        ),
        (
            "Our Commitment",
            {
                "fields": (
                    "commitment_title",
                    "commitment_content",
                )
            },
        ),
        (
            "Organogram",
            {
                "fields": (
                    "organogram_image",
                    "organogram_alt_text",
                    "organogram_description",
                )
            },
        ),
    )


@admin.register(JourneyMilestone)
class JourneyMilestoneAdmin(admin.ModelAdmin):

    list_display = [
        "year",
        "title",
        "ordering",
        "is_published",
    ]

    list_filter = [
        "year",
        "is_published",
    ]

    search_fields = [
        "title",
        "short_description",
        "description",
    ]

    ordering = [
        "year",
        "ordering",
    ]

    fieldsets = (
        (
            "Milestone",
            {
                "fields": (
                    "year",
                    "title",
                    "short_description",
                    "description",
                )
            },
        ),
        (
            "Image",
            {
                "fields": (
                    "image",
                    "image_alt_text",
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


@admin.register(GovernanceOverview)
class GovernanceOverviewAdmin(admin.ModelAdmin):

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
        "introduction",
        "strategic_governing_tier",
        "executive_secretariat",
        "field_management",
        "reporting_structure",
    ]

    fieldsets = (
        (
            "Governance",
            {
                "fields": (
                    "title",
                    "introduction",
                )
            },
        ),
        (
            "Organisational Structure",
            {
                "fields": (
                    "strategic_governing_tier",
                    "executive_secretariat",
                    "field_management",
                    "reporting_structure",
                )
            },
        ),
        (
            "Additional Information",
            {
                "fields": (
                    "governance_note",
                    "is_published",
                )
            },
        ),
    )