from django.contrib import admin

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "partner_type",
        "ordering",
        "is_active",
    ]

    list_filter = [
        "partner_type",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
    ]

    ordering = [
        "partner_type",
        "ordering",
        "name",
    ]

    fieldsets = (
        (
            "Partner Information",
            {
                "fields": (
                    "name",
                    "partner_type",
                    "description",
                )
            },
        ),
        (
            "Branding & Link",
            {
                "fields": (
                    "logo",
                    "website_url",
                    "accessibility_alt_text",
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