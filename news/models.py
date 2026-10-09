from django.db import models
from django.utils.text import slugify


class NewsArticle(models.Model):

    CATEGORY_CHOICES = [
        ("news", "News"),
        ("field_story", "Field Story"),
        ("analysis", "Thematic Analysis"),
        ("announcement", "Announcement"),
        ("staff_voice", "Staff Voice"),
    ]

    title = models.CharField(max_length=250)

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="news"
    )

    excerpt = models.TextField(
        help_text="Short summary shown on news listing cards."
    )

    content = models.TextField()

    featured_image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True
    )

    image_alt_text = models.CharField(
        max_length=250,
        blank=True,
        help_text="Accessible description of the image."
    )

    author_name = models.CharField(
        max_length=150,
        blank=True
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=False
    )

    ordering = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "-is_featured",
            "-published_at",
            "ordering",
            "-created_at",
        ]
        verbose_name = "News Article"
        verbose_name_plural = "News Articles"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
