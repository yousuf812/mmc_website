from django import forms

from .models import ContactEnquiry


class ContactEnquiryForm(forms.ModelForm):

    class Meta:
        model = ContactEnquiry

        fields = [
            "name",
            "email",
            "phone",
            "organization",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your email address",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Your phone number",
                }
            ),

            "organization": forms.TextInput(
                attrs={
                    "class": "form-input",
                    "placeholder": "Organisation",
                }
            ),

            "subject": forms.Select(
                attrs={
                    "class": "form-input",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "placeholder": "Write us what you want to know...",
                    "rows": 6,
                }
            ),
        }