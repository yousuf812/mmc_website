from django.contrib import admin

from .models import (
    ContactSettings,
    ContactEnquiry,
)


@admin.register(ContactSettings)
class ContactSettingsAdmin(admin.ModelAdmin):

    list_display = [
        "email",
        "phone_1",
        "phone_2",
        "is_active",
        "updated_at",
    ]

    list_filter = [
        "is_active",
    ]

    fieldsets = (
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone_1",
                    "phone_2",
                    "office_address",
                )
            },
        ),
        (
            "Contact Page",
            {
                "fields": (
                    "contact_intro",
                    "is_active",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        if ContactSettings.objects.exists():
            return False

        return super().has_add_permission(request)


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "email",
        "organization",
        "subject",
        "status",
        "created_at",
    ]

    list_filter = [
        "subject",
        "status",
        "created_at",
    ]

    search_fields = [
        "name",
        "email",
        "organization",
        "message",
    ]

    readonly_fields = [
        "name",
        "email",
        "phone",
        "organization",
        "subject",
        "message",
        "created_at",
        "updated_at",
    ]

    fieldsets = (
        (
            "Visitor Information",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                    "organization",
                )
            },
        ),
        (
            "Enquiry",
            {
                "fields": (
                    "subject",
                    "message",
                )
            },
        ),
        (
            "Administration",
            {
                "fields": (
                    "status",
                    "admin_notes",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )