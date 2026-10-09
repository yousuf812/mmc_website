from django.db import models


class ContactSettings(models.Model):

    email = models.EmailField(
        default="connect@mmcintnl.org"
    )

    phone_1 = models.CharField(
        max_length=50,
        default="(+254) 728478178"
    )

    phone_2 = models.CharField(
        max_length=50,
        default="(+252) 618472031"
    )

    office_address = models.TextField(
        default=(
            "Airport Road, Wadajir District, "
            "Mogadishu, Banadir, Somalia"
        )
    )

    contact_intro = models.TextField(
        blank=True,
        default=(
            "Let’s talk about what’s possible. Whether you are "
            "a donor, a partner, a volunteer, client, or someone "
            "who simply wants to understand our work better, "
            "we would love to hear from you."
        )
    )

    is_active = models.BooleanField(
        default=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Contact Settings"
        verbose_name_plural = "Contact Settings"

    def __str__(self):
        return "MMC Contact Settings"


class ContactEnquiry(models.Model):

    SUBJECT_CHOICES = [
        ("general", "General Enquiry"),
        ("donor", "Donor"),
        ("partner", "Partnership"),
        ("volunteer", "Volunteer"),
        ("client", "Client / Customer"),
        ("supplier", "Supplier / Contractor"),
        ("career", "Career"),
        ("media", "Media"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    organization = models.CharField(
        max_length=200,
        blank=True
    )

    subject = models.CharField(
        max_length=30,
        choices=SUBJECT_CHOICES,
        default="general"
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    admin_notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "-created_at",
        ]
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"