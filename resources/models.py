from django.db import models
from django.utils.text import slugify


class Publication(models.Model):

    ACCESS_LEVEL_CHOICES = [
        ("public", "Public"),
        ("registered", "Registered Users"),
        ("on_request", "On Request"),
        ("members_only", "Members Only"),
        ("view_only", "View Only"),
    ]

    title = models.CharField(
        max_length=250
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    description = models.TextField()

    cover_image = models.ImageField(
        upload_to="publications/covers/",
        blank=True,
        null=True
    )

    image_alt_text = models.CharField(
        max_length=250,
        blank=True
    )

    document = models.FileField(
        upload_to="publications/documents/",
        blank=True,
        null=True
    )

    access_level = models.CharField(
        max_length=20,
        choices=ACCESS_LEVEL_CHOICES,
        default="public"
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

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class GalleryItem(models.Model):

    MEDIA_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
    ]

    title = models.CharField(
        max_length=250
    )

    media_type = models.CharField(
        max_length=10,
        choices=MEDIA_TYPE_CHOICES,
        default="image"
    )

    image = models.ImageField(
        upload_to="gallery/images/",
        blank=True,
        null=True
    )

    video_file = models.FileField(
        upload_to="gallery/videos/",
        blank=True,
        null=True
    )

    video_url = models.URLField(
        blank=True
    )

    caption = models.TextField(
        blank=True
    )

    alt_text = models.CharField(
        max_length=250,
        blank=True
    )

    consent_cleared = models.BooleanField(
        default=False,
        help_text="Confirm that required photography/video consent has been cleared."
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
            "ordering",
            "-created_at",
        ]

    def __str__(self):
        return self.title


class PressKitItem(models.Model):

    ITEM_TYPE_CHOICES = [
        ("logo", "Logo"),
        ("photo", "Executive Photo"),
        ("biography", "Executive Biography"),
        ("video", "Video"),
        ("document", "Document"),
    ]

    title = models.CharField(
        max_length=250
    )

    item_type = models.CharField(
        max_length=20,
        choices=ITEM_TYPE_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    file = models.FileField(
        upload_to="press-kit/",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="press-kit/images/",
        blank=True,
        null=True
    )

    external_url = models.URLField(
        blank=True
    )

    alt_text = models.CharField(
        max_length=250,
        blank=True
    )

    consent_cleared = models.BooleanField(
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
            "ordering",
            "-created_at",
        ]

    def __str__(self):
        return self.title