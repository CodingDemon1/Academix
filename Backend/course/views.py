from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from instructors.models import Instructor
from course.models import Course
import json


@csrf_exempt
def add_course(request):
    if request.method == "POST":
        data = json.loads(request.body)
        instructor = Instructor.objects.get(id=data["instructor_id"])
        course = Course(
            course_code=data["course_code"],
            course_name=data["course_name"],
            department=data["department"],
            credits=data["credits"],
            description=data["description"],
            instructor=instructor,
        )
        course.save()
        return JsonResponse({"message": "Course added successfully", "response": True})


@csrf_exempt
def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        instructor = Instructor.objects.get(id=data["instructor_id"])
        course.course_code = data["course_code"]
        course.course_name = data["course_name"]
        course.department = data["department"]
        course.credits = data["credits"]
        course.description = data["description"]
        course.instructor = instructor
        course.save()
        return JsonResponse(
            {"message": "Course updated successfully", "response": True}
        )


@csrf_exempt
def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return JsonResponse(
            {"message": "Course not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        course.delete()
        return JsonResponse(
            {"message": "Course deleted successfully", "response": True}
        )


@csrf_exempt
def get_course_by_id(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        course_data = {
            "id": course.id,
            "course_code": course.course_code,
            "course_name": course.course_name,
            "department": course.department,
            "credits": course.credits,
            "description": course.description,
            "instructor": course.instructor.name,
        }
        return JsonResponse({"course": course_data, "response": True})
    except Course.DoesNotExist:
        return JsonResponse(
            {"message": "Course not found", "response": False}, status=404
        )


@csrf_exempt
def get_courses(request):
    if request.method == "GET":
        courses = Course.objects.all()
        course_data = [
            {
                "id": course.id,
                "course_code": course.course_code,
                "course_name": course.course_name,
                "department": course.department,
                "credits": course.credits,
                "description": course.description,
                "instructor": course.instructor.name,
            }
            for course in courses
        ]
        return JsonResponse({"courses": course_data, "response": True})


@csrf_exempt
def courses_by_instructor(request, instructor_id):
    try:
        instructor_courses = Course.objects.filter(instructor_id=instructor_id)
        courses_data = [
            {
                "course_code": course.course_code,
                "course_name": course.course_name,
                "department": course.department,
                "credits": course.credits,
                "description": course.description,
                "id": course.id,
                "instructor_id": course.instructor.id,
            }
            for course in instructor_courses
        ]
        return JsonResponse({"courses": courses_data, "response": True})
    except Exception as e:
        return JsonResponse({"error": str(e), "response": False}, status=500)


# Add the rest of the views
