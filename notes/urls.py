from django.urls import path
from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("note/<int:pk>/", views.note_detail, name="note_detail"),
    path("create/", views.note_create, name="note_create"),
    path("note/<int:pk>/update/", views.note_update, name="note_update"),
    path("note/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
