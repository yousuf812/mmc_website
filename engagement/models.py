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
    OPPORTUNITY_TYPES = [
        ("volunteer", "Volunteer"),
        ("internship", "Internship"),
        ("staff", "Staff / Career"),
        ("consultant", "Consultant"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    
    # Image er table onujayi notun fields
    opportunity_type = models.CharField(
        max_length=30, 
        choices=OPPORTUNITY_TYPES, 
        default="volunteer"
    )
    area = models.CharField(
        max_length=150, 
        blank=True, 
        help_text="e.g. Field support, Skills & livelihood, Communications"
    )
    location = models.CharField(
        max_length=150, 
        blank=True, 
        help_text="e.g. Baidoa, Mogadishu, Remote"
    )
    commitment = models.CharField(
        max_length=150, 
        blank=True, 
        help_text="e.g. Part-time, 3 months / Flexible, 5 hrs/week"
    )
    
    description = models.TextField()
    responsibilities = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    application_instructions = models.TextField(blank=True)
    application_email = models.EmailField(blank=True)
    application_url = models.URLField(blank=True)
    deadline = models.DateField(blank=True, null=True)

    is_open = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.get_opportunity_type_display()})"


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




class JobApplication(models.Model):

    class ApplicationStatus(models.TextChoices):
        RECEIVED = "received", "Received"
        UNDER_REVIEW = "under_review", "Under Review"
        SHORTLISTED = "shortlisted", "Shortlisted"
        REJECTED = "rejected", "Rejected"
        HIRED = "hired", "Hired"

    vacancy = models.ForeignKey(
        JobVacancy,
        on_delete=models.PROTECT,
        related_name="applications",
    )

    full_name = models.CharField(
        max_length=200,
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
    )

    area_of_expertise = models.CharField(
        max_length=255,
    )

    sector = models.CharField(
        max_length=150,
    )

    language = models.CharField(
        max_length=255,
        help_text="Languages you speak, e.g. English, Bangla.",
    )

    availability = models.CharField(
        max_length=150,
        help_text="e.g. Full-time, Part-time, Immediate, or 2 weeks.",
    )

    cv_or_sample_work = models.FileField(
        upload_to="engagement/job_applications/",
    )

    daily_rate_expectation = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Optional daily rate expectation.",
    )

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.RECEIVED,
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"

    def __str__(self):
        return f"{self.full_name} — {self.vacancy.title}"


# volunteerr application

class VolunteerApplication(models.Model):

    class ApplicationStatus(models.TextChoices):
        RECEIVED = "received", "Received"
        UNDER_REVIEW = "under_review", "Under Review"
        SHORTLISTED = "shortlisted", "Shortlisted"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"

    opportunity = models.ForeignKey(
        VolunteerOpportunity,
        on_delete=models.PROTECT,
        related_name="applications",
    )

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=30)

    location = models.CharField(
        max_length=200,
        blank=True,
    )

    skills_and_experience = models.TextField(
        help_text="Describe your relevant skills and experience.",
    )

    motivation = models.TextField(
        help_text="Why would you like to volunteer with MMC?",
    )

    availability = models.CharField(
        max_length=200,
        help_text="e.g. Weekends, weekdays, or specific hours.",
    )

    cv_or_supporting_document = models.FileField(
        upload_to="engagement/volunteer_applications/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.RECEIVED,
    )

    submitted_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Volunteer Application"
        verbose_name_plural = "Volunteer Applications"

    def __str__(self):
        return f"{self.full_name} — {self.opportunity.title}"

