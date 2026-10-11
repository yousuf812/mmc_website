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

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        input_classes = (
            "block w-full rounded-xl border border-slate-300 "
            "bg-white px-4 py-3 text-sm text-slate-900 "
            "placeholder:text-slate-400 "
            "transition duration-200 "
            "focus:border-blue-600 focus:outline-none "
            "focus:ring-4 focus:ring-blue-100"
        )

        for field_name, field in self.fields.items():
            if field_name == "message":
                field.widget.attrs.update({
                    "class": input_classes + " min-h-36 resize-y",
                    "placeholder": "Write your message here...",
                    "rows": 5,
                })

            else:
                field.widget.attrs.update({
                    "class": input_classes,
                })

        self.fields["name"].widget.attrs["placeholder"] = "Enter your full name"
        self.fields["email"].widget.attrs["placeholder"] = "you@example.com"
        self.fields["phone"].widget.attrs["placeholder"] = "Enter your phone number"
        self.fields["organization"].widget.attrs["placeholder"] = "Your organisation name"
        self.fields["subject"].widget.attrs["placeholder"] = "What is your enquiry about?"



