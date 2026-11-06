from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator


class EngagementPage(models.Model):

    PAGE_TYPE_CHOICES = [
        ("volunteer", "Volunteer"),
        ("careers", "Work with us"),
        ("partnerships", "Partner with us"),
        ("donate", "Fund us"),
        ("suppliers", "Supply for us"),
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

    # টেবিলের View/Download ফিচারের জন্য এই ফিল্ডটি এখানে যোগ করা হয়েছে
    document = models.FileField(
        upload_to="engagement/opportunities/documents/",
        blank=True,
        null=True,
        verbose_name="Opportunity Document",
        help_text="Upload one PDF or other supporting document."
    )

    is_open = models.BooleanField(default=True)
    ordering = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "-created_at"]
        verbose_name = "Opportunity"
        verbose_name_plural = "Opportunities"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.get_opportunity_type_display()})"



class JobVacancy(models.Model):

    TYPE_CHOICES = [
        ("jobs", "Jobs"),
        ("internships", "Internships"),
        ("consulting", "Consulting"),
        ("volunteer", "Volunteer"),
    ]

    LOCATION_CHOICES = [
        ("Mogadishu", "Mogadishu"),
        ("Baidoa", "Baidoa"),
        ("Remote", "Remote"),
        ("Somalia", "Somalia"),
        ("International", "International"),
    ]

    FUNCTIONAL_AREA_CHOICES = [
        ("programmes_field_operations", "Programmes & Field Operations"),
        ("technical_sectors_service_delivery", "Technical Sectors & Service Delivery"),
        ("protection_safeguarding_inclusion", "Protection, Safeguarding & Inclusion"),
        ("meal", "MEAL"),
        ("research_data_analytics", "Research & Data Analytics"),
        ("advocacy_policy_communications", "Advocacy, Policy & Communications"),
        ("fundraising_partnerships_donor_relations", "Fundraising, Partnerships & Donor Relations"),
        ("finance_accounting_audit", "Finance, Accounting & Audit"),
        ("human_resources_administration", "Human Resources & Administration"),
        ("logistics_procurement_supply_chain", "Logistics, Procurement & Supply Chain"),
        ("technology_it_digital_innovation", "Technology, IT & Digital Innovation"),
        ("governance_risk_compliance_security", "Governance, Risk, Compliance & Security"),
        ("engineering_infrastructure_environment", "Engineering, Infrastructure & Environment"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("open", "Open"),
        ("closing_soon", "Closing Soon"),
        ("deadline_extended", "Deadline Extended"),
        ("readvertised", "Re-advertised"),
        ("closed", "Closed"),
        ("cancelled", "Cancelled"),
        ("filled", "Filled"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    # Keep old field temporarily for existing data compatibility
    department = models.CharField(
        max_length=150,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        choices=LOCATION_CHOICES,
        blank=True
    )

    employment_type = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        blank=True
    )

    functional_area = models.CharField(
        max_length=100,
        choices=FUNCTIONAL_AREA_CHOICES,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="open"
    )

    description = models.TextField()

    responsibilities = models.TextField(blank=True)

    qualifications = models.TextField(blank=True)

    experience = models.TextField(blank=True)

    application_instructions = models.TextField(blank=True)

    application_email = models.EmailField(blank=True)

    application_url = models.URLField(blank=True)

    closing_date = models.DateField(
        blank=True,
        null=True
    )

    # Keep temporarily for compatibility with existing code
    is_open = models.BooleanField(default=True)

    ordering = models.PositiveIntegerField(default=0)

    circular_document = models.FileField(
        upload_to="job_circulars/%Y/%m/",
        blank=True,
        null=True,
        help_text="Upload official circular (PDF, DOC, DOCX, PNG, JPG)",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf", "doc", "docx", "jpg", "jpeg", "png"]
            )
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordering", "-created_at"]
        verbose_name = "Job Vacancy"
        verbose_name_plural = "Job Vacancies"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        # Keep legacy is_open field synchronized with the new status
        self.is_open = self.status not in ["closed", "cancelled", "filled"]

        super().save(*args, **kwargs)

    @property
    def can_apply(self):
        return self.status not in ["closed", "cancelled", "filled"]

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
        help_text="Languages you speak, e.g. English, Somali.",
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



class MMCTestimonial(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    location = models.CharField(max_length=150)

    photo = models.ImageField(
        upload_to="testimonials/",
        help_text="Upload testimonial person's photograph."
    )

    quote = models.TextField()

    ordering = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "MMC Testimonial"
        verbose_name_plural = "Voices of MMC"
        ordering = ["ordering", "-created_at"]

    def __str__(self):
        return self.name
