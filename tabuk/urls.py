from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("packages", views.package, name="packages"),
    path("booking/<package_slug>", views.booking, name="book"),
    path('checkout/<int:book_id>', views.checkout, name="checkout"),
]