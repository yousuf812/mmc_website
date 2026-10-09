from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactEnquiryForm
from .models import ContactSettings


def contact(request):

    settings = (
        ContactSettings.objects
        .filter(is_active=True)
        .first()
    )

    if request.method == "POST":

        form = ContactEnquiryForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Thank you. Your enquiry has been submitted successfully."
            )

            return redirect("contact:contact")

    else:

        form = ContactEnquiryForm()

    context = {
        "contact_settings": settings,
        "form": form,
    }

    return render(
        request,
        "contact/contact.html",
        context
    )