from pages.models import SiteSettings


def site_settings_context(request):
    settings = SiteSettings.objects.filter(
        is_active=True
    ).first()

    return {
        "site_settings": settings,
    }