# Add imports at the beginning of your urls.py
from . import views
from django.urls import path, include

urlpatterns = [
    # ...
    path("add/", views.add_course, name="add_course"),
    path("update/<int:course_id>/", views.update_course, name="update_course"),
    path("delete/<int:course_id>/", views.delete_course, name="delete_course"),
    path("<int:course_id>/", views.get_course_by_id, name="get_course_by_id"),
    path(
        "get-instructor-id/<int:instructor_id>/",
        views.courses_by_instructor,
        name="courses_by_instructor",
    ),
    path("", views.get_courses, name="get_all_courses"),
    # Add other URL mappings
]
