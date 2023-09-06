from django.urls import path
from . import views

urlpatterns = [
    # ...
    path("add/", views.add_assignment, name="add_assignment"),
    path(
        "update/<int:assignment_id>/",
        views.update_assignment,
        name="update_assignment",
    ),
    path(
        "delete/<int:assignment_id>/",
        views.delete_assignment,
        name="delete_assignment",
    ),
    path(
        "<int:assignment_id>/",
        views.get_assignment_by_id,
        name="get_assignment_by_id",
    ),
    path(
        "get-by-course-id/<int:course_id>/",
        views.get_assignment_by_course_id,
        name="get_assignment_by_course_id",
    ),
    path("", views.get_all_assignments, name="get_all_assignments"),
    # Add other URL mappings
]
