from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Student, Course, Enrollment
from assignment.models import Assignment
import json


# Add other imports if necessary
@csrf_exempt
def enroll_student_in_course(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student_id = data.get("student_id")
        course_id = data.get("course_id")

        if student_id is None or course_id is None:
            return JsonResponse(
                {"message": "Student ID and Course ID are required", "response": False},
                status=400,
            )

        student = get_object_or_404(Student, id=student_id)
        course = get_object_or_404(Course, id=course_id)

        enrollment = Enrollment(student=student, course=course)
        enrollment.save()

        return JsonResponse(
            {"message": "Enrollment added successfully", "response": True}
        )


def get_enrollments_for_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        enrollments = Enrollment.objects.filter(student=student)
        enrollment_data = [
            {
                "id": enrollment.id,
                "course_id": enrollment.id,
                "course_name": enrollment.course.course_name,  # Include course name
                "course_department": enrollment.course.department,
                "enrollment_date": enrollment.enrollment_date.strftime("%Y-%m-%d"),
            }
            for enrollment in enrollments
        ]

        return JsonResponse({"enrollments": enrollment_data, "response": True})
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )


def get_enrollments_for_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        enrollments = Enrollment.objects.filter(course=course)

        enrollment_data = [
            {
                "id": enrollment.id,
                "student_id": enrollment.student_id,
                "enrollment_date": enrollment.enrollment_date.strftime("%Y-%m-%d"),
            }
            for enrollment in enrollments
        ]

        return JsonResponse({"enrollments": enrollment_data, "response": True})
    except Course.DoesNotExist:
        return JsonResponse(
            {"message": "Course not found", "response": False}, status=404
        )


def get_assignments_for_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        enrolled_courses = (
            student.enrollment_set.all()
        )  # Retrieve courses the student is enrolled in
        course_ids = enrolled_courses.values_list(
            "course_id", flat=True
        )  # Get course IDs

        assignments = Assignment.objects.filter(course_id__in=course_ids)
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

        return JsonResponse({"response": True, "assignments": assignment_data})
    except Student.DoesNotExist:
        return JsonResponse(
            {"response": False, "message": "Student not found"}, status=404
        )
