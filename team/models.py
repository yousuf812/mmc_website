from django.db import models


class TeamMember(models.Model):

    class TeamCategory(models.TextChoices):
        BOARD = "board", "Board of Trustees & Strategic Advisers"
        MANAGEMENT = "management", "Management"
        FIELD = "field", "Field"

    name = models.CharField(
        max_length=200,
    )

    title = models.CharField(
        max_length=255,
    )

    category = models.CharField(
        max_length=30,
        choices=TeamCategory.choices,
    )

    photograph = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True,
    )

    academic_qualification = models.TextField(
        blank=True,
    )

    technical_background = models.TextField(
        blank=True,
    )

    mandate = models.TextField(
        blank=True,
    )

    linkedin_url = models.URLField(
        blank=True,
        help_text="Use only an approved LinkedIn profile URL.",
    )

    accessibility_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Descriptive alternative text for the team photograph.",
    )

    biography = models.TextField(
        blank=True,
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
            "category",
            "ordering",
            "name",
        ]

        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.name} - {self.title}"