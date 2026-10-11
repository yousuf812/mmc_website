from django.urls import path

from . import views

app_name = "tenders"

urlpatterns = [
path("", views.tender_list, name="list"),
# path("[slug:slug](slug:slug)/", views.tender_detail, name="detail"),
 path("<slug:slug>/", views.tender_detail, name="detail"),
path("[slug:slug](slug:slug)/document/",views.tender_document,name="document",),
]
