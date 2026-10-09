from django.db import models
from django.utils.text import slugify


class EngagementPage(models.Model):

    PAGE_TYPE_CHOICES = [
        ("volunteer", "Volunteer"),
        ("careers", "Careers"),
        ("partnerships", "Partnerships"),
        ("donate", "Donate & Support"),
        ("clients", "Customers / Clients"),
        ("suppliers", "Suppliers & Contractors"),
    ]

    page_type = models.CharField(
        max_length=30,
        choices=PAGE_TYPE_CHOICES,
        unique=True
    )

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    short_description = models.TextField(
        blank=True
    )

    content = models.TextField(
        blank=True
    )

    why_engage = models.TextField(
        blank=True,
        help_text="Explain why someone should engage with MMC through this section."
    )

    process = models.TextField(
        blank=True,
        help_text="Explain the engagement/application process."
    )

    requirements = models.TextField(
        blank=True,
        help_text="Relevant requirements or information needed from the visitor."
    )

    call_to_action = models.CharField(
        max_length=150,
        blank=True
    )

    call_to_action_url = models.URLField(
        blank=True
    )

    featured_image = models.ImageField(
        upload_to="engagement/",
        blank=True,
        null=True
    )

    image_alt_text = models.CharField(
        max_length=250,
        blank=True
    )

    is_published = models.BooleanField(
        default=True
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
            "title",
        ]
        verbose_name = "Engagement Page"
        verbose_name_plural = "Engagement Pages"

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class VolunteerOpportunity(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField()

    responsibilities = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    application_instructions = models.TextField(
        blank=True
    )

    application_email = models.EmailField(
        blank=True
    )

    application_url = models.URLField(
        blank=True
    )

    deadline = models.DateField(
        blank=True,
        null=True
    )

    is_open = models.BooleanField(
        default=True
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
            "title",
        ]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class JobVacancy(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    department = models.CharField(
        max_length=150,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        blank=True
    )

    employment_type = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField()

    responsibilities = models.TextField(
        blank=True
    )

    qualifications = models.TextField(
        blank=True
    )

    experience = models.TextField(
        blank=True
    )

    application_instructions = models.TextField(
        blank=True
    )

    application_email = models.EmailField(
        blank=True
    )

    application_url = models.URLField(
        blank=True
    )

    closing_date = models.DateField(
        blank=True,
        null=True
    )

    is_open = models.BooleanField(
        default=True
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

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title