from django.urls import path
from . import views

urlpatterns = [
    path("", views.fetch_html, name="fetch_html"),
]