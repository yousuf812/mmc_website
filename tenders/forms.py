
from pathlib import Path

from django import forms

from .models import SupplierRegistration


class SupplierRegistrationForm(forms.ModelForm):

    class Meta:
        model = SupplierRegistration
        fields = [
            "company_name",
            "email",
            "registration_number",
            "supply_category",
            "registration_document",
        ]

        widgets = {
            "company_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Enter your company name",
                "autocomplete": "organization",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "company@example.com",
                "autocomplete": "email",
            }),
            "registration_number": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Enter registration number",
            }),
            "supply_category": forms.Select(attrs={
                "class": "form-input",
            }),
            "registration_document": forms.ClearableFileInput(attrs={
                "class": "form-input",
                "accept": ".pdf,application/pdf",
            }),
        }

    def clean_registration_document(self):
        uploaded_file = self.cleaned_data.get(
            "registration_document"
        )

        if not uploaded_file:
            raise forms.ValidationError(
                "Please upload your company registration document."
            )

        extension = Path(uploaded_file.name).suffix.lower()

        if extension != ".pdf":
            raise forms.ValidationError(
                "Only PDF documents are accepted."
            )

        if uploaded_file.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "The document must not exceed 5 MB."
            )

        return uploaded_file
