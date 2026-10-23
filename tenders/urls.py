from django.urls import path
from . import views

app_name = "tenders"

urlpatterns = [
    path("", views.tender_list, name="list"),
    path(
        "<slug:slug>/",
        views.tender_detail,
        name="detail",
    ),
    path(
        "<slug:slug>/document/",
        views.tender_document,
        name="document",
    ),
    # মূল আবেদন লিঙ্ক (আপনার টেমপ্লেটের url 'tenders:apply' এর সাথে মিল রেখে)
    path(
        "<slug:slug>/apply/",
        views.apply_tender_view,
        name="apply",
    ),
]