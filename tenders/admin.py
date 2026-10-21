from django.contrib import admin
from django.utils import timezone

from .models import Tender, SupplierRegistration

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):

    list_display = (
        "reference",
        "title",
        "category",
        "closing_date",
        "status",             # editable field — must be here
        "display_status",     # computed display
        "is_published",
    )

    list_filter = (
        "category",
        "status",
        "is_published",
        "closing_date",
    )

    search_fields = (
        "reference",
        "title",
        "description",
    )

    list_editable = (
        "status",
        "is_published",
    )

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
    )

    date_hierarchy = "closing_date"
    ordering = ("closing_date", "reference")
    list_per_page = 25

    fieldsets = (
        (
            "Tender Information",
            {
                "fields": (
                    "reference",
                    "title",
                    "slug",
                    "category",
                    "description",
                )
            },
        ),
        (
            "Dates and Status",
            {
                "fields": (
                    "published_date",
                    "closing_date",
                    "status",
                    "is_published",
                )
            },
        ),
        (
            "Tender Document",
            {"fields": ("document",)},
        ),
        (
            "System Information",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Effective status", ordering="status")
    def display_status(self, obj):
        return obj.effective_status



@admin.register(SupplierRegistration)
class SupplierRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "email",
        "registration_number",
        "tender",
        "supply_category",
        "status",
        "submitted_at",
    )

    list_filter = (
        "supply_category",
        "status",
        "submitted_at",
    )

    search_fields = (
        "company_name",
        "email",
        "registration_number",
        "tender__reference",
        "tender__title",
    )

    readonly_fields = (
        "submitted_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Tender Information",
            {
                "fields": ("tender",),
            },
        ),
        (
            "Company Information",
            {
                "fields": (
                    "company_name",
                    "email",
                    "registration_number",
                    "supply_category",
                ),
            },
        ),
        (
            "Registration Document",
            {
                "fields": ("registration_document",),
            },
        ),
        (
            "Application Review",
            {
                "fields": (
                    "status",
                    "submitted_at",
                    "updated_at",
                ),
            },
        ),
    )

    ordering = ("-submitted_at",)
    list_per_page = 25


    # Optional: delete this if `ordering` attribute is enough
    # def get_queryset(self, request):
    #     return super().get_queryset(request).order_by(
    #         "closing_date", "reference"
    #     )