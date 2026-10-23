
from pathlib import Path
from django import forms
from .models import SupplierRegistration
from .models import BidSubmission


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





class BidSubmissionForm(forms.ModelForm):
    is_subject_to_sanctions = forms.ChoiceField(
        choices=[("NO", "NO"), ("YES", "YES")],
        widget=forms.RadioSelect(attrs={"class": "sanction-radio-input"}),
        required=True,
    )

    class Meta:
        model = BidSubmission
        fields = [
            "company_name",
            "authorized_representative",
            "email",
            "telephone_number",
            "business_registration_number",
            "financial_proposal",
            "technical_proposal",
            "declare_accuracy_authorization",
            "declare_eligibility_integrity",
            "declare_conflict_interest",
            "declare_sanctions",
            "is_subject_to_sanctions",
            "sanctions_details",
            "declare_terms_code_of_conduct",
            "declare_verification_submission",
        ]
        widgets = {
            "company_name": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "Enter registered company name",
            }),
            "authorized_representative": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "Full legal name of authorized person",
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "official.contact@company.com",
            }),
            "telephone_number": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "+880 1XXXXXXXXX",
            }),
            "business_registration_number": forms.TextInput(attrs={
                "class": "w-full rounded-xl border border-slate-300 bg-white px-4 py-3 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "Registration / Trade License number",
            }),
            "financial_proposal": forms.ClearableFileInput(attrs={
                "class": "block w-full cursor-pointer text-sm text-slate-500 file:mr-4 file:rounded-lg file:border-0 file:bg-slate-100 file:px-4 file:py-2.5 file:text-xs file:font-bold file:text-slate-700 hover:file:bg-slate-200",
                "accept": ".pdf,application/pdf",
            }),
            "technical_proposal": forms.ClearableFileInput(attrs={
                "class": "block w-full cursor-pointer text-sm text-slate-500 file:mr-4 file:rounded-lg file:border-0 file:bg-slate-100 file:px-4 file:py-2.5 file:text-xs file:font-bold file:text-slate-700 hover:file:bg-slate-200",
                "accept": ".zip,application/zip,application/x-zip-compressed",
            }),
            "sanctions_details": forms.Textarea(attrs={
                "rows": 3,
                "class": "w-full rounded-xl border border-slate-300 bg-white p-3.5 text-sm font-medium text-slate-800 placeholder-slate-400 focus:border-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-700/20",
                "placeholder": "Specify the organization, reason, date, duration, and current status...",
            }),
            "declare_accuracy_authorization": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
            "declare_eligibility_integrity": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
            "declare_conflict_interest": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
            "declare_sanctions": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
            "declare_terms_code_of_conduct": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
            "declare_verification_submission": forms.CheckboxInput(attrs={"class": "h-5 w-5 rounded border-slate-300 text-teal-700 focus:ring-teal-600"}),
        }

    def clean_financial_proposal(self):
        uploaded_file = self.cleaned_data.get("financial_proposal")
        if not uploaded_file:
            raise forms.ValidationError("Please upload the signed Financial Proposal (PDF).")

        ext = Path(uploaded_file.name).suffix.lower()
        if ext != ".pdf":
            raise forms.ValidationError("Financial proposal must be in PDF format only.")

        if uploaded_file.size > 20 * 1024 * 1024:
            raise forms.ValidationError("Financial proposal file size cannot exceed 20 MB.")

        return uploaded_file

    def clean_technical_proposal(self):
        uploaded_file = self.cleaned_data.get("technical_proposal")
        if not uploaded_file:
            raise forms.ValidationError("Please upload the technical proposal and supporting documents (ZIP).")

        ext = Path(uploaded_file.name).suffix.lower()
        if ext != ".zip":
            raise forms.ValidationError("Supporting documents must be packaged in a single .zip file.")

        if uploaded_file.size > 50 * 1024 * 1024:
            raise forms.ValidationError("ZIP package size cannot exceed 50 MB.")

        return uploaded_file

    def clean(self):
        cleaned_data = super().clean()

        # All declarations must be checked
        declarations = [
            "declare_accuracy_authorization",
            "declare_eligibility_integrity",
            "declare_conflict_interest",
            "declare_sanctions",
            "declare_terms_code_of_conduct",
            "declare_verification_submission",
        ]
        for field in declarations:
            if not cleaned_data.get(field):
                self.add_error(field, "You must agree to this declaration to proceed.")

        # Conditional validation for Sanctions
        is_sanctioned = cleaned_data.get("is_subject_to_sanctions") == "YES"
        cleaned_data["is_subject_to_sanctions"] = is_sanctioned
        details = cleaned_data.get("sanctions_details")

        if is_sanctioned and not details:
            self.add_error("sanctions_details", "Mandatory: Please provide the explanation and details of the sanction/suspension.")

        return cleaned_data
