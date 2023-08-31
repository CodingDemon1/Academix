from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    # ...
    path("add/", views.add_instructor, name="add_instructor"),
    path("", views.get_instructors, name="get_instructors"),
    path(
        "update/<int:instructor_id>/",
        views.update_instructor,
        name="update_instructor",
    ),
    path(
        "delete/<int:instructor_id>/",
        views.delete_instructor,
        name="delete_instructor",
    ),
    path(
        "<int:instructor_id>/",
        views.get_instructor_by_id,
        name="get_instructor_by_id",
    ),
]
