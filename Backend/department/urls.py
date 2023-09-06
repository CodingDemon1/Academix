from django.urls import path
from . import views

urlpatterns = [
    # ... Your existing URL mappings ...
    # Create Department
    path("add/", views.create_department, name="create_department"),
    # Get All Departments
    path("", views.get_all_departments, name="get_all_departments"),
    # Update Department
    path(
        "update/<int:department_id>/",
        views.update_department,
        name="update_department",
    ),
    # Delete Department
    path(
        "delete/<int:department_id>/",
        views.delete_department,
        name="delete_department",
    ),
    # Get Department by ID
    path(
        "<int:department_id>/",
        views.get_department_by_id,
        name="get_department_by_id",
    ),
]
