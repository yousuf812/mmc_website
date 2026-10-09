from django.db import models


class Partner(models.Model):

    class PartnerType(models.TextChoices):
        CLIENT = "client", "Clients / Implementation Partners"
        PROGRAMME = "programme", "Programmes / Consortiums"
        FUNDER = "funder", "Funding Partners"

    name = models.CharField(
        max_length=255,
    )

    partner_type = models.CharField(
        max_length=30,
        choices=PartnerType.choices,
    )

    description = models.TextField(
        blank=True,
    )

    logo = models.ImageField(
        upload_to="partners/",
        blank=True,
        null=True,
    )

    website_url = models.URLField(
        blank=True,
    )

    accessibility_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Descriptive alternative text for the partner logo.",
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "partner_type",
            "ordering",
            "name",
        ]

        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name