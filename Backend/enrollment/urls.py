from django.urls import path
from . import views

urlpatterns = [
    # Enroll Student in Course
    path("", views.enroll_student_in_course, name="enroll_student_in_course"),
    # Get Enrollments for Student
    path(
        "student/<int:student_id>/",
        views.get_enrollments_for_student,
        name="get_enrollments_for_student",
    ),
    # Get Enrollments for Course
    path(
        "course/<int:course_id>/",
        views.get_enrollments_for_course,
        name="get_enrollments_for_course",
    ),
    path(
        "get-assignments-by-stId/<int:student_id>/",
        views.get_assignments_for_student,
        name="get_assignments_for_student",
    ),
    # ... Other URL mappings ...
]
