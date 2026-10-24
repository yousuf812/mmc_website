from django.db import models

class HeroSlide(models.Model):
    title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional title for this slide."
    )

    image = models.ImageField(
        upload_to="homepage/hero-slides/",
        help_text="Upload the background image for this slide."
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Describe the image for accessibility."
    )

    is_active = models.BooleanField(default=True)

    ordering = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["ordering", "-created_at"]
        verbose_name = "Hero Slide"
        verbose_name_plural = "Hero Slides"

    def __str__(self):
        return self.title or f"Hero Slide {self.pk}"

