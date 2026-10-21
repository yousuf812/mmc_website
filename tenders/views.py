from datetime import timedelta
from mimetypes import guess_type
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import FileResponse, Http404
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SupplierRegistrationForm
from .models import Tender

def tender_list(request):
    today = timezone.localdate()
    closing_soon_date = today + timedelta(days=14)

    all_published = Tender.objects.filter(is_published=True)

    tenders = all_published.order_by("closing_date", "reference")

    search_query = request.GET.get("q", "").strip()
    if search_query:
        tenders = tenders.filter(
            Q(title__icontains=search_query)
            | Q(reference__icontains=search_query)
        )

    selected_category = request.GET.get("category", "").strip()
    valid_categories = {
        value for value, label in Tender.Category.choices
    }

    if selected_category in valid_categories:
        tenders = tenders.filter(category=selected_category)
    else:
        selected_category = ""

    selected_status = request.GET.get("status", "").strip()
    valid_statuses = {
        value for value, label in Tender.Status.choices
    }

    if selected_status in valid_statuses:
        if selected_status == Tender.Status.OPEN:
            tenders = tenders.filter(
                status=Tender.Status.OPEN,
                closing_date__gte=today,
            )
        elif selected_status == Tender.Status.CLOSED:
            tenders = tenders.filter(
                Q(status=Tender.Status.CLOSED)
                | Q(
                    status=Tender.Status.OPEN,
                    closing_date__lt=today,
                )
            )
        else:
            tenders = tenders.filter(status=selected_status)
    else:
        selected_status = ""

    paginator = Paginator(tenders, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    open_count = all_published.filter(
        status=Tender.Status.OPEN,
        closing_date__gte=today,
    ).count()

    closing_soon_count = all_published.filter(
        status=Tender.Status.OPEN,
        closing_date__gte=today,
        closing_date__lte=closing_soon_date,
    ).count()

    closed_count = all_published.filter(
        Q(status=Tender.Status.CLOSED)
        | Q(
            status=Tender.Status.OPEN,
            closing_date__lt=today,
        )
    ).count()

    awarded_count = all_published.filter(
        status=Tender.Status.AWARDED
    ).count()

    context = {
        "tenders": page_obj.object_list,
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_category": selected_category,
        "selected_status": selected_status,
        "categories": Tender.Category.choices,
        "statuses": Tender.Status.choices,
        "open_count": open_count,
        "closing_soon_count": closing_soon_count,
        "closed_count": closed_count,
        "awarded_count": awarded_count,
    }

    return render(request, "tenders/tender_list.html", context)

def tender_detail(request, slug):
    tender = get_object_or_404(
    Tender,
    slug=slug,
    is_published=True,
    )


    return render(
        request,
        "tenders/tender_detail.html",
        {"tender": tender},
    )


def tender_document(request, slug):
    tender = get_object_or_404(
    Tender,
    slug=slug,
    is_published=True,
    )


    if not tender.document:
        raise Http404("Tender document is not available.")

    try:
        file_handle = tender.document.open("rb")
    except (OSError, ValueError):
        raise Http404("Tender document is not available.")

    filename = tender.document.name.rsplit("/", 1)[-1]
    content_type, _ = guess_type(filename)

    response = FileResponse(
        file_handle,
        as_attachment=True,
        filename=filename,
        content_type=content_type or "application/octet-stream",
    )

    response["X-Content-Type-Options"] = "nosniff"
    return response





def supplier_registration(request, slug):
    tender = get_object_or_404(
        Tender,
        slug=slug,
        is_published=True,
    )

    if tender.effective_status != Tender.Status.OPEN:
        messages.error(
            request,
            "Applications are not available for this tender.",
        )
        return redirect(
            "tenders:tender_detail",
            slug=tender.slug,
        )

    if request.method == "POST":
        form = SupplierRegistrationForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            registration = form.save(commit=False)
            registration.tender = tender
            registration.save()

            messages.success(
                request,
                "Your supplier registration has been submitted successfully.",
            )

            return redirect(
                  "tenders:detail",
                  slug=tender.slug,
            )
    else:
        form = SupplierRegistrationForm()

    return render(
        request,
        "tenders/supplier_registration.html",
        {
            "tender": tender,
            "form": form,
        },
    )


