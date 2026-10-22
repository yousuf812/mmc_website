
from pathlib import Path

from django import forms

from .models import JobApplication
from .models import VolunteerApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "full_name",
            "email",
            "phone",
            "area_of_expertise",
            "sector",
            "language",
            "availability",
            "cv_or_sample_work",
            "daily_rate_expectation",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "placeholder": "Enter your full name",
                "autocomplete": "name",
                "class": "form-input",
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
                "class": "form-input",
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "Enter your phone number",
                "autocomplete": "tel",
                "class": "form-input",
            }),

            "area_of_expertise": forms.TextInput(attrs={
                "placeholder": "e.g. Project Management, Engineering",
                "class": "form-input",
            }),

            "sector": forms.TextInput(attrs={
                "placeholder": "e.g. Humanitarian, Infrastructure, Health",
                "class": "form-input",
            }),

            "language": forms.TextInput(attrs={
                "placeholder": "e.g. English, Bangla",
                "class": "form-input",
            }),

            "availability": forms.TextInput(attrs={
                "placeholder": "e.g. Full-time, Part-time, Immediate",
                "class": "form-input",
            }),

            "cv_or_sample_work": forms.ClearableFileInput(attrs={
                "class": "form-input",
                "accept": ".pdf,.doc,.docx",
            }),

            "daily_rate_expectation": forms.NumberInput(attrs={
                "placeholder": "Enter expected daily rate (optional)",
                "min": "0",
                "step": "0.01",
                "class": "form-input",
            }),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()

        if len(phone) < 7 or len(phone) > 30:
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone

    def clean_cv_or_sample_work(self):
        uploaded_file = self.cleaned_data.get("cv_or_sample_work")

        if not uploaded_file:
            raise forms.ValidationError(
                "Please upload your CV or sample work."
            )

        allowed_extensions = {".pdf", ".doc", ".docx"}
        extension = Path(uploaded_file.name).suffix.lower()

        if extension not in allowed_extensions:
            raise forms.ValidationError(
                "Upload a PDF, DOC, or DOCX file."
            )

        max_size = 5 * 1024 * 1024

        if uploaded_file.size > max_size:
            raise forms.ValidationError(
                "The file must not exceed 5 MB."
            )

        return uploaded_file


class VolunteerApplicationForm(forms.ModelForm):

    class Meta:
        model = VolunteerApplication

        fields = [
            "full_name",
            "email",
            "phone",
            "location",
            "skills_and_experience",
            "motivation",
            "availability",
            "cv_or_supporting_document",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Enter your full name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "Enter your email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Enter your phone number",
            }),
            "location": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "City or country",
            }),
            "skills_and_experience": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 4,
                "placeholder": "Describe your relevant skills and experience",
            }),
            "motivation": forms.Textarea(attrs={
                "class": "form-input",
                "rows": 4,
                "placeholder": "Why would you like to volunteer with MMC?",
            }),
            "availability": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "e.g. Weekends or weekdays",
            }),
        }

    def clean_cv_or_supporting_document(self):
        uploaded_file = self.cleaned_data.get(
            "cv_or_supporting_document"
        )

        if uploaded_file:
            max_size = 5 * 1024 * 1024  # 5 MB

            if uploaded_file.size > max_size:
                raise forms.ValidationError(
                    "File size must not exceed 5 MB."
                )

            allowed_extensions = (".pdf", ".doc", ".docx")

            filename = uploaded_file.name.lower()

            if not filename.endswith(allowed_extensions):
                raise forms.ValidationError(
                    "Only PDF, DOC, and DOCX files are allowed."
                )

        return uploaded_file
