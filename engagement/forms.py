
from pathlib import Path

from django import forms

from .models import JobApplication


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
