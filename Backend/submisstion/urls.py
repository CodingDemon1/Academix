from django.urls import path
from . import views

urlpatterns = [
    # ... Your existing URL mappings ...
    # Submit Assignment
    path("", views.submit_assignment, name="submit_assignment"),
    # Get Submissions for Assignment
    path(
        "assignment/<int:assignment_id>/",
        views.get_submissions_for_assignment,
        name="get_submissions_for_assignment",
    ),
    # Get Submissions for Student
    path(
        "student/<int:student_id>/",
        views.get_submissions_for_student,
        name="get_submissions_for_student",
    ),
    # ... Other URL mappings ...
]
