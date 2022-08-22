from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entry, name="entry"),
    path("random", views.Random, name="random"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new"),
    path("save", views.save, name="save"),
    path("edit", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit"),
]
