from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Tender(models.Model):

    class Category(models.TextChoices):
        GOODS = "goods", "Goods"
        SERVICES = "services", "Services"
        WORKS = "works", "Works"
        CONSULTANCY = "consultancy", "Consultancy"

    class Status(models.TextChoices):
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"
        AWARDED = "awarded", "Awarded"

    reference = models.CharField(
        max_length=50,
        unique=True,
        help_text="Example: MMC/T/2026/011",
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.SERVICES,
    )

    description = models.TextField(blank=True)

    published_date = models.DateField(
        default=timezone.localdate,
    )

    closing_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )

    document = models.FileField(
        upload_to="tenders/documents/",
        blank=True,
        null=True,
        help_text="Upload the official tender document.",
    )

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["closing_date", "reference"]
        verbose_name = "Tender"
        verbose_name_plural = "Tenders"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.reference) or "tender"
            candidate = base_slug
            counter = 1

            while Tender.objects.filter(slug=candidate).exclude(
                pk=self.pk
            ).exists():
                counter += 1
                candidate = f"{base_slug}-{counter}"

            self.slug = candidate

        super().save(*args, **kwargs)

    @property
    def effective_status(self):
        if self.status == self.Status.AWARDED:
            return self.Status.AWARDED

        if self.status == self.Status.CLOSED:
            return self.Status.CLOSED

        if self.closing_date < timezone.localdate():
            return self.Status.CLOSED

        return self.Status.OPEN

    def get_effective_status_display(self):
        return dict(self.Status.choices).get(
            self.effective_status,
            self.effective_status,
        )

    @property
    def is_closing_soon(self):
        today = timezone.localdate()
        days_left = (self.closing_date - today).days

        return (
            self.status == self.Status.OPEN
            and 0 <= days_left <= 14
        )

    def __str__(self):
        return f"{self.reference} — {self.title}"