from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json

from .models import Announcement


# Create your views here.
@csrf_exempt
def create_announcement(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        publish_date = data.get("publish_date")
        department_id = data.get("department_id")
        course_id = data.get("course_id")

        if (
            title is None
            or description is None
            or publish_date is None
            or department_id is None
            or course_id is None
        ):
            return JsonResponse(
                {
                    "message": "Title, Description, Publish Date, Department ID, and Course ID are required",
                    "response": False,
                },
                status=400,
            )

        announcement = Announcement(
            title=title,
            description=description,
            publish_date=publish_date,
            department_id=department_id,
            course_id=course_id,
        )
        announcement.save()

        return JsonResponse(
            {"message": "Announcement created successfully", "response": True}
        )


def get_all_announcements(request):
    announcements = Announcement.objects.all()

    announcement_data = [
        {
            "id": announcement.id,
            "title": announcement.title,
            "description": announcement.description,
            "publish_date": announcement.publish_date.strftime("%Y-%m-%d"),
            "department_id": announcement.department_id,
            "course_id": announcement.course_id,
        }
        for announcement in announcements
    ]

    return JsonResponse({"announcements": announcement_data, "response": True})


def get_announcement_by_id(request, announcement_id):
    try:
        announcement = Announcement.objects.get(id=announcement_id)
        announcement_data = {
            "id": announcement.id,
            "title": announcement.title,
            "description": announcement.description,
            "publish_date": announcement.publish_date.strftime("%Y-%m-%d"),
            "department_id": announcement.department_id,
            "course_id": announcement.course_id,
        }
        return JsonResponse({"announcement": announcement_data, "response": True})
    except Announcement.DoesNotExist:
        return JsonResponse(
            {"message": "Announcement not found", "response": False}, status=404
        )


@csrf_exempt
def update_announcement(request, announcement_id):
    announcement = get_object_or_404(Announcement, id=announcement_id)
    if request.method == "PUT":
        data = json.loads(request.body)
        title = data.get("title")
        description = data.get("description")
        publish_date = data.get("publish_date")
        department_id = data.get("department_id")
        course_id = data.get("course_id")

        if title is not None:
            announcement.title = title
        if description is not None:
            announcement.description = description
        if publish_date is not None:
            announcement.publish_date = publish_date
        if department_id is not None:
            announcement.department_id = department_id
        if course_id is not None:
            announcement.course_id = course_id

        announcement.save()

        return JsonResponse(
            {"message": "Announcement updated successfully", "response": True}
        )


@csrf_exempt
def delete_announcement(request, announcement_id):
    try:
        announcement = Announcement.objects.get(id=announcement_id)
    except Announcement.DoesNotExist:
        return JsonResponse(
            {"message": "Announcement not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        announcement.delete()
        return JsonResponse(
            {"message": "Announcement deleted successfully", "response": True}
        )
