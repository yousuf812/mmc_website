from django.db import models


class ProjectPriority(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = "Project Priority"
        verbose_name_plural = "Project Priorities"

    def __str__(self):
        return self.name


class ProjectSector(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = "Project Sector"
        verbose_name_plural = "Project Sectors"

    def __str__(self):
        return self.name


class SDG(models.Model):

    number = models.PositiveIntegerField(
        unique=True,
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    icon = models.ImageField(
        upload_to="sdgs/",
        blank=True,
        null=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "SDG"
        verbose_name_plural = "SDGs"

    def __str__(self):
        return f"SDG {self.number} - {self.title}"


class DeliveryEngine(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = "Delivery Engine"
        verbose_name_plural = "Delivery Engines"

    def __str__(self):
        return self.name


class Project(models.Model):

    class ProjectStatus(models.TextChoices):
        PLANNED = "planned", "Planned"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"
        ARCHIVED = "archived", "Archived"

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
    )

    project_code = models.CharField(
        max_length=150,
        blank=True,
        help_text="Optional project or contract reference.",
    )

    short_description = models.TextField(
        help_text="Short description for project cards and listings.",
    )

    description = models.TextField(
        blank=True,
    )

    featured_image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )

    image_alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Accessibility description for the project image.",
    )

    priority = models.ForeignKey(
        ProjectPriority,
        on_delete=models.PROTECT,
        related_name="projects",
    )

    sectors = models.ManyToManyField(
        ProjectSector,
        blank=True,
        related_name="projects",
    )

    sdgs = models.ManyToManyField(
        SDG,
        blank=True,
        related_name="projects",
    )

    delivery_engines = models.ManyToManyField(
        DeliveryEngine,
        blank=True,
        related_name="projects",
    )

    location = models.CharField(
        max_length=255,
        blank=True,
    )

    country = models.CharField(
        max_length=100,
        default="Somalia",
    )

    client_donor = models.CharField(
        max_length=255,
        blank=True,
    )

    start_date = models.DateField(
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    project_status = models.CharField(
        max_length=20,
        choices=ProjectStatus.choices,
        default=ProjectStatus.ACTIVE,
    )

    outcomes = models.TextField(
        blank=True,
    )

    impact_summary = models.TextField(
        blank=True,
    )

    beneficiaries = models.TextField(
        blank=True,
    )

    success_story = models.TextField(
        blank=True,
    )

    testimonial = models.TextField(
        blank=True,
    )

    testimonial_name = models.CharField(
        max_length=200,
        blank=True,
    )

    testimonial_role = models.CharField(
        max_length=255,
        blank=True,
    )

    video_url = models.URLField(
        blank=True,
    )

    baseline_report = models.FileField(
        upload_to="projects/reports/",
        blank=True,
        null=True,
    )

    final_report = models.FileField(
        upload_to="projects/reports/",
        blank=True,
        null=True,
    )

    endline_report = models.FileField(
        upload_to="projects/reports/",
        blank=True,
        null=True,
    )

    predecessor_note = models.TextField(
        blank=True,
        help_text="Use when explaining predecessor/MMCI experience where relevant.",
    )

    is_featured = models.BooleanField(
        default=False,
    )

    is_published = models.BooleanField(
        default=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = [
            "-is_featured",
            "ordering",
            "-start_date",
            "title",
        ]

        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title


class PriorityAction(models.Model):
    """
    Areas of focus and action under each strategic priority.
    """

    priority = models.ForeignKey(
        "pages.StrategicPriority",
        on_delete=models.CASCADE,
        related_name="actions",
    )

    title = models.CharField(
        max_length=250
    )

    description = models.TextField(
        blank=True
    )

    ordering = models.PositiveIntegerField(
        default=0
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "priority",
            "ordering",
            "title",
        ]

        verbose_name = "Priority Action"
        verbose_name_plural = "Priority Actions"

    def __str__(self):
        return f"{self.priority.name} - {self.title}"



class WhatWeDoPage(models.Model):
    """
    Main CMS content for the What We Do page.
    """

    title = models.CharField(
        max_length=200,
        default="What We Do"
    )

    subtitle = models.CharField(
        max_length=300,
        default="From humanitarian action to resilience, opportunity and self-reliance."
    )

    why_mmc_title = models.CharField(
        max_length=200,
        default="Why MMC Exists"
    )

    why_mmc_content = models.TextField()

    model_title = models.CharField(
        max_length=200,
        default="The MMC Model of Change 2026-2030"
    )

    model_description = models.TextField()

    priorities_intro = models.TextField(
        blank=True
    )

    delivery_intro = models.TextField(
        blank=True
    )

    commitments_title = models.CharField(
        max_length=200,
        default="Cross-Cutting Commitments"
    )

    commitments_intro = models.TextField(
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "What We Do Page"
        verbose_name_plural = "What We Do Page"

    def __str__(self):
        return self.title


class CrossCuttingCommitment(models.Model):
    """
    Organisation-wide standards applied across all MMC work.
    """

    title = models.CharField(
        max_length=200
    )

    standard = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon name/class for the frontend."
    )

    ordering = models.PositiveIntegerField(
        default=0
    )

    is_published = models.BooleanField(
        default=True
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

        verbose_name = "Cross-Cutting Commitment"
        verbose_name_plural = "Cross-Cutting Commitments"

    def __str__(self):
        return self.title