from django.contrib import admin

from .models import (
    Publication,
    GalleryItem,
    PressKitItem,
)


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "access_level",
        "published_at",
        "is_featured",
        "is_published",
        "ordering",
    ]

    list_filter = [
        "access_level",
        "is_featured",
        "is_published",
        "published_at",
    ]

    search_fields = [
        "title",
        "description",
    ]

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = [
        "-published_at",
        "-created_at",
    ]

    date_hierarchy = "published_at"

    fieldsets = (
        (
            "Publication Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                )
            },
        ),
        (
            "Files and Image",
            {
                "fields": (
                    "cover_image",
                    "image_alt_text",
                    "document",
                )
            },
        ),
        (
            "Access Control",
            {
                "fields": (
                    "access_level",
                )
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "published_at",
                    "is_featured",
                    "is_published",
                    "ordering",
                )
            },
        ),
    )


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "media_type",
        "consent_cleared",
        "is_published",
        "ordering",
    ]

    list_filter = [
        "media_type",
        "consent_cleared",
        "is_published",
    ]

    search_fields = [
        "title",
        "caption",
        "alt_text",
    ]

    ordering = [
        "ordering",
        "-created_at",
    ]

    fieldsets = (
        (
            "Media Information",
            {
                "fields": (
                    "title",
                    "media_type",
                    "image",
                    "video_file",
                    "video_url",
                )
            },
        ),
        (
            "Accessibility",
            {
                "fields": (
                    "caption",
                    "alt_text",
                )
            },
        ),
        (
            "Consent & Publishing",
            {
                "fields": (
                    "consent_cleared",
                    "is_published",
                    "ordering",
                )
            },
        ),
    )


@admin.register(PressKitItem)
class PressKitItemAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "item_type",
        "consent_cleared",
        "is_published",
        "ordering",
    ]

    list_filter = [
        "item_type",
        "consent_cleared",
        "is_published",
    ]

    search_fields = [
        "title",
        "description",
        "alt_text",
    ]

    ordering = [
        "ordering",
        "-created_at",
    ]

    fieldsets = (
        (
            "Press Kit Information",
            {
                "fields": (
                    "title",
                    "item_type",
                    "description",
                )
            },
        ),
        (
            "Media",
            {
                "fields": (
                    "file",
                    "image",
                    "external_url",
                    "alt_text",
                )
            },
        ),
        (
            "Consent & Publishing",
            {
                "fields": (
                    "consent_cleared",
                    "is_published",
                    "ordering",
                )
            },
        ),
    )