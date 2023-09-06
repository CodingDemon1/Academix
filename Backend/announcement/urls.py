from django.urls import path
from . import views


urlpatterns = [
    # ... Your existing URL mappings ...
    # Create Announcement
    path("add/", views.create_announcement, name="create_announcement"),
    # Get All Announcements
    path("", views.get_all_announcements, name="get_all_announcements"),
    # Get Announcement by ID
    path(
        "<int:announcement_id>/",
        views.get_announcement_by_id,
        name="get_announcement_by_id",
    ),
    # Update Announcement
    path(
        "<int:announcement_id>/",
        views.update_announcement,
        name="update_announcement",
    ),
    # Delete Announcement
    path(
        "<int:announcement_id>/",
        views.delete_announcement,
        name="delete_announcement",
    ),
    # ... Other URL mappings ...
]
