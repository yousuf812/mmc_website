from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(
        max_length=200,
        default="Mission for Meaningful Change",
    )

    tagline = models.CharField(
        max_length=255,
        default="From vulnerability to self-reliance",
    )

    logo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True,
    )

    favicon = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True,
    )

    announcement_enabled = models.BooleanField(
        default=True,
    )

    announcement_text = models.CharField(
        max_length=255,
        default="MMCI is now MMC: same people, same mission, new legal form",
    )

    email = models.EmailField(
        default="connect@mmcintnl.org",
    )

    phone_1 = models.CharField(
        max_length=50,
        default="(+254) 728478178",
    )

    phone_2 = models.CharField(
        max_length=50,
        default="(+252) 618472031",
    )

    address = models.TextField(
        default="Airport Road, Wadajir District, Mogadishu, Banadir, Somalia",
    )

    facebook_url = models.URLField(
        blank=True,
    )

    linkedin_url = models.URLField(
        blank=True,
    )

    youtube_url = models.URLField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class Homepage(models.Model):
    hero_title = models.CharField(
        max_length=255,
        default="From vulnerability to self-reliance",
    )

    hero_description = models.TextField(
        blank=True,
    )

    hero_image = models.ImageField(
        upload_to="homepage/",
        blank=True,
        null=True,
    )

    hero_primary_button_text = models.CharField(
        max_length=100,
        default="Explore our work",
    )

    hero_primary_button_url = models.CharField(
        max_length=255,
        default="/our-work/",
    )

    hero_secondary_button_text = models.CharField(
        max_length=100,
        default="Partner with MMC",
    )

    hero_secondary_button_url = models.CharField(
        max_length=255,
        default="/get-involved/partnerships/",
    )

    hero_donate_button_text = models.CharField(
        max_length=100,
        default="Donate",
    )

    hero_donate_button_url = models.CharField(
        max_length=255,
        default="/get-involved/donate/",
    )

    mission_title = models.CharField(
        max_length=255,
        default="Our Mission",
    )

    mission_text = models.TextField(
        blank=True,
    )

    vision_title = models.CharField(
        max_length=255,
        default="Our Vision",
    )

    vision_text = models.TextField(
        blank=True,
    )

    closing_cta_title = models.CharField(
        max_length=255,
        blank=True,
    )

    closing_cta_text = models.TextField(
        blank=True,
    )

    closing_cta_button_text = models.CharField(
        max_length=100,
        blank=True,
    )

    closing_cta_button_url = models.CharField(
        max_length=255,
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

    def __str__(self):
        return self.hero_title


class StrategicPriority(models.Model):

    number = models.PositiveIntegerField(
        default=1,
    )

    title = models.CharField(
        max_length=255,
    )

    short_description = models.TextField()

    full_description = models.TextField(
        blank=True,
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon name.",
    )

    image = models.ImageField(
        upload_to="priorities/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        ordering = ["ordering", "number"]
        verbose_name = "Strategic Priority"
        verbose_name_plural = "Strategic Priorities"

    def __str__(self):
        return f"{self.number}. {self.title}"


class ImpactStatistic(models.Model):

    value = models.CharField(
        max_length=50,
    )

    label = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
    )

    ordering = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["ordering"]
        verbose_name = "Impact Statistic"
        verbose_name_plural = "Impact Statistics"

    def __str__(self):
        return f"{self.value} - {self.label}"



class AboutPage(models.Model):
    """
    CMS content for the Who We Are / About MMC page.
    """

    title = models.CharField(
        max_length=200,
        default="Who We Are"
    )

    subtitle = models.CharField(
        max_length=300,
        default="One institution. A new legal form. A lasting mission."
    )

    about_title = models.CharField(
        max_length=200,
        default="About MMC"
    )

    about_content = models.TextField()

    purpose_title = models.CharField(
        max_length=200,
        default="Our Purpose"
    )

    purpose_content = models.TextField()

    mission_title = models.CharField(
        max_length=200,
        default="Our Mission"
    )

    mission_content = models.TextField()

    vision_title = models.CharField(
        max_length=200,
        default="Our Vision"
    )

    vision_content = models.TextField()

    commitment_title = models.CharField(
        max_length=200,
        default="Our Commitment"
    )

    commitment_content = models.TextField(
        help_text="Use one commitment per line."
    )

    featured_image = models.ImageField(
        upload_to="pages/about/",
        blank=True,
        null=True
    )

    image_alt_text = models.CharField(
        max_length=300,
        blank=True
    )

    organogram_image = models.ImageField(
        upload_to="pages/organogram/",
        blank=True,
        null=True
    )

    organogram_alt_text = models.CharField(
        max_length=500,
        blank=True
    )

    organogram_description = models.TextField(
        blank=True,
        help_text="Text-only description for screen readers."
    )

    is_published = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    @property
    def commitments(self):
        return [
            item.strip()
            for item in self.commitment_content.splitlines()
            if item.strip()
        ]

    def __str__(self):
        return self.title


class JourneyMilestone(models.Model):
    """
    Timeline milestones for MMC's institutional journey.
    """

    year = models.PositiveIntegerField()

    title = models.CharField(
        max_length=200
    )

    short_description = models.CharField(
        max_length=500,
        blank=True
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="pages/journey/",
        blank=True,
        null=True
    )

    image_alt_text = models.CharField(
        max_length=300,
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
            "year",
            "ordering",
        ]

        verbose_name = "Journey Milestone"
        verbose_name_plural = "Journey Milestones"

    def __str__(self):
        return f"{self.year} - {self.title}"


class GovernanceOverview(models.Model):
    """
    Governance and structural overview content.
    """

    title = models.CharField(
        max_length=200,
        default="Governance & Structural Overview"
    )

    introduction = models.TextField()

    strategic_governing_tier = models.TextField(
        blank=True
    )

    executive_secretariat = models.TextField(
        blank=True
    )

    field_management = models.TextField(
        blank=True
    )

    reporting_structure = models.TextField(
        blank=True
    )

    governance_note = models.TextField(
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Governance Overview"
        verbose_name_plural = "Governance Overview"

    def __str__(self):
        return self.title