from django.contrib import admin
from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "category",
        "author_name",
        "published_at",
        "is_featured",
        "is_published",
        "ordering",
    ]

    list_filter = [
        "category",
        "is_featured",
        "is_published",
        "published_at",
    ]

    search_fields = [
        "title",
        "excerpt",
        "content",
        "author_name",
    ]

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = [
        "-published_at",
        "-created_at",
    ]

    

    fieldsets = (
        (
            "Article Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "excerpt",
                    "content",
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
                    "author_name",
                    "published_at",
                    "is_featured",
                    "is_published",
                    "ordering",
                )
            },
        ),
    )