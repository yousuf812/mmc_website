from django.shortcuts import get_object_or_404, render

from .models import Publication, GalleryItem, PressKitItem


def publication_list(request):
    publications = (
        Publication.objects
        .filter(is_published=True)
        .order_by("-is_featured", "-published_at", "ordering")
    )

    return render(
        request,
        "resources/publication_list.html",
        {"publications": publications},
    )


def publication_detail(request, slug):
    publication = get_object_or_404(
        Publication,
        slug=slug,
        is_published=True,
    )

    return render(
        request,
        "resources/publication_detail.html",
        {"publication": publication},
    )


def gallery_list(request):
    gallery_items = (
        GalleryItem.objects
        .filter(
            is_published=True,
            consent_cleared=True,
        )
        .order_by("ordering", "-created_at")
    )

    return render(
        request,
        "resources/gallery.html",
        {
            "gallery_items": gallery_items,
        },
    )


def press_kit(request):
    press_kit_items = (
        PressKitItem.objects
        .filter(
            is_published=True,
            consent_cleared=True,
        )
        .order_by("ordering", "-created_at")
    )

    return render(
        request,
        "resources/press_kit.html",
        {
            "press_kit_items": press_kit_items,
        },
    )