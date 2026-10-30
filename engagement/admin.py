from django.contrib import admin


from .models import (
    EngagementPage,
    VolunteerOpportunity,
    JobVacancy,
    JobApplication,
    VolunteerApplication
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
        "opportunity_type",
        "area",
        "location",
        "commitment",
        "deadline",
        "is_open",
        "ordering",
    ]
    list_filter = [
        "opportunity_type",
        "is_open",
        "area",
        "location",
        "deadline",
    ]
    search_fields = [
        "title",
        "area",
        "location",
        "description",
        "requirements",
    ]
    prepopulated_fields = {"slug": ("title",)}
    ordering = ["ordering", "title"]

    fieldsets = (
        ("Opportunity Information", {
            "fields": (
                "title",
                "slug",
                "opportunity_type",
                "area",
                "location",
                "commitment",
                "description",
            )
        }),
        ("Role Details", {
            "fields": (
                "responsibilities",
                "requirements",
            )
        }),
        ("Application", {
            "fields": (
                "application_instructions",
                "application_email",
                "application_url",
                "deadline",
            )
        }),
        ("Status & Ordering", {
            "fields": (
                "is_open",
                "ordering",
            )
        }),
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

    @admin.display(boolean=True, description="Circular Attached")
    def has_document(self, obj):
        return bool(obj.circular_document)





@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = [
        "full_name",
        "vacancy",
        "email",
        "phone",
        "sector",
        "status",
        "submitted_at",
    ]

    list_filter = [
        "status",
        "sector",
        "availability",
        "submitted_at",
    ]

    search_fields = [
        "full_name",
        "email",
        "phone",
        "area_of_expertise",
        "sector",
        "vacancy__title",
    ]

    readonly_fields = [
        "submitted_at",
        "updated_at",
    ]

    list_editable = [
        "status",
    ]

    list_select_related = [
        "vacancy",
    ]

    date_hierarchy = "submitted_at"
    ordering = ["-submitted_at"]
    list_per_page = 25

    fieldsets = (
        (
            "Job Information",
            {
                "fields": (
                    "vacancy",
                ),
            },
        ),
        (
            "Applicant Information",
            {
                "fields": (
                    "full_name",
                    "email",
                    "phone",
                    "area_of_expertise",
                    "sector",
                    "language",
                    "availability",
                    "daily_rate_expectation",
                ),
            },
        ),
        (
            "CV / Sample Work",
            {
                "fields": (
                    "cv_or_sample_work",
                ),
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




@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "opportunity",
        "email",
        "phone",
        "status",
        "submitted_at",
    )

    list_filter = (
        "status",
        "opportunity",
        "submitted_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "opportunity__title",
    )

    readonly_fields = (
        "submitted_at",
        "updated_at",
    )

    list_per_page = 25

    fieldsets = (
        (
            "Applicant Information",
            {
                "fields": (
                    "opportunity",
                    "full_name",
                    "email",
                    "phone",
                    "location",
                ),
            },
        ),
        (
            "Volunteer Details",
            {
                "fields": (
                    "skills_and_experience",
                    "motivation",
                    "availability",
                    "cv_or_supporting_document",
                ),
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

