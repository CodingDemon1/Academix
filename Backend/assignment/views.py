from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from course.models import Course
from assignment.models import Assignment
import json


@csrf_exempt
def add_assignment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        course = Course.objects.get(id=data["course_id"])
        assignment = Assignment(
            course=course,
            title=data["title"],
            description=data["description"],
            due_date=data["dueDate"],
        )
        assignment.save()
        return JsonResponse(
            {"message": "Assignment added successfully", "response": True}
        )


# Add the rest of the views


@csrf_exempt
def update_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        course = get_object_or_404(Course, id=data["course_id"])
        assignment.course = course
        assignment.title = data["title"]
        assignment.description = data["description"]
        assignment.due_date = data["dueDate"]
        assignment.save()
        return JsonResponse(
            {"message": "Assignment updated successfully", "response": True}
        )


@csrf_exempt
def delete_assignment(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
    except Assignment.DoesNotExist:
        return JsonResponse(
            {"message": "Assignment not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        assignment.delete()
        return JsonResponse(
            {"message": "Assignment deleted successfully", "response": True}
        )


@csrf_exempt
def get_assignment_by_course_id(request, course_id):
    try:
        course = get_object_or_404(Course, id=course_id)
        course_assignments = Assignment.objects.filter(course=course)
        assignments_data = [
            {
                "id": assignment.id,
                "title": assignment.title,
                "description": assignment.description,
                "dueDate": assignment.due_date.strftime("%Y-%m-%d"),
            }
            for assignment in course_assignments
        ]
        return JsonResponse({"assignment": assignments_data, "response": True})
    except Assignment.DoesNotExist:
        return JsonResponse(
            {"message": "Assignment not found", "response": False}, status=404
        )


@csrf_exempt
def get_assignment_by_id(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        assignment_data = {
            "id": assignment.id,
            "course_id": assignment.course_id,
            "title": assignment.title,
            "description": assignment.description,
            "due_date": assignment.due_date.strftime("%Y-%m-%d"),
        }
        return JsonResponse({"assignment": assignment_data, "response": True})
    except Assignment.DoesNotExist:
        return JsonResponse(
            {"message": "Assignment not found", "response": False}, status=404
        )


def get_all_assignments(request):
    assignments = Assignment.objects.all()

    assignment_data = [
        {
            "id": assignment.id,
            "course_id": assignment.course_id,
            "title": assignment.title,
            "description": assignment.description,
            "due_date": assignment.due_date.strftime("%Y-%m-%d"),
        }
        for assignment in assignments
    ]

    return JsonResponse({"assignments": assignment_data, "response": True})
