from django.contrib import admin
from .models import HeroSlide
from django.utils.html import format_html

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image_preview",
        "is_active",
        "ordering",
        "created_at",
    )

    list_filter = ("is_active",)
    search_fields = ("title", "alt_text")
    list_editable = ("is_active", "ordering")
    ordering = ("ordering", "-created_at")

    fields = (
        "title",
        "image",
        "alt_text",
        "is_active",
        "ordering",
    )

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="120" '
                'style="height:60px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "No image"

    image_preview.short_description = "Preview"

