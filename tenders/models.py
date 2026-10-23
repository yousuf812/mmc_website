from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import uuid
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



# registration

class SupplierRegistration(models.Model):

    class SupplyCategory(models.TextChoices):
        GOODS = "goods", "Goods Supply"
        SERVICES = "services", "Services"
        WORKS = "works", "Works"
        CONSULTANCY = "consultancy", "Consultancy"

    class ApplicationStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        UNDER_REVIEW = "under_review", "Under Review"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    tender = models.ForeignKey(
        Tender,
        on_delete=models.PROTECT,
        related_name="supplier_registrations",
    )

    company_name = models.CharField(max_length=255)

    email = models.EmailField()

    registration_number = models.CharField(
        max_length=100,
    )

    supply_category = models.CharField(
        max_length=20,
        choices=SupplyCategory.choices,
    )

    registration_document = models.FileField(
        upload_to="tenders/registrations/",
    )

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING,
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-submitted_at"]
        verbose_name = "Supplier Registration"
        verbose_name_plural = "Supplier Registrations"

    def __str__(self):
        return f"{self.company_name} — {self.tender.reference}"




# new bid code



def financial_upload_path(instance, filename):
    return f"bids/{instance.tender_reference}/financial/{instance.submission_reference}_{filename}"


def technical_upload_path(instance, filename):
    return f"bids/{instance.tender_reference}/technical/{instance.submission_reference}_{filename}"


class BidSubmission(models.Model):
    # Unique Submission Reference & Metadata
    submission_reference = models.CharField(
        max_length=32, unique=True, editable=False, db_index=True
    )
    submitted_at = models.DateTimeField(default=timezone.now, editable=False)

    # 1. Tender Details
    tender_reference = models.CharField(max_length=100, editable=False)
    tender_title = models.CharField(max_length=255, editable=False)
    closing_datetime = models.DateTimeField(editable=False)

    # 2. Bidder Information
    company_name = models.CharField(max_length=255)
    authorized_representative = models.CharField(max_length=255)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=50)
    business_registration_number = models.CharField(
        max_length=100, blank=True, null=True
    )

    # 3. Two-Envelope Uploads
    financial_proposal = models.FileField(
        upload_to=financial_upload_path,
        help_text="Signed financial proposal in PDF format only.",
    )
    technical_proposal = models.FileField(
        upload_to=technical_upload_path,
        help_text="Technical proposal and all supporting documents in single ZIP format.",
    )

    # 4. Declarations
    declare_accuracy_authorization = models.BooleanField(default=False)
    declare_eligibility_integrity = models.BooleanField(default=False)
    declare_conflict_interest = models.BooleanField(default=False)
    declare_sanctions = models.BooleanField(default=False)
    
    # Sanction Question & Conditional Detail
    is_subject_to_sanctions = models.BooleanField(
        choices=[(True, "YES"), (False, "NO")],
        help_text="Is your company/organization currently subject to sanctions/suspensions?",
    )
    sanctions_details = models.TextField(
        blank=True,
        null=True,
        help_text="If YES, specify organization, reason, date, duration, and status.",
    )

    declare_terms_code_of_conduct = models.BooleanField(default=False)
    declare_verification_submission = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.submission_reference:
            # MMC-YYYYMMDD-UUID 
            self.submission_reference = f"MMC-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.submission_reference} - {self.company_name} ({self.tender_reference})"
