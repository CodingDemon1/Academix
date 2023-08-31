from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student


@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student(
            name=data["name"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            major=data["major"],
            email=data["email"],
            contact_number=data["contact_number"],
            password=data["password"],  # Not recommended for real-world use
        )
        student.save()
        return JsonResponse({"message": "Student added successfully", "response": True})


@csrf_exempt
def get_students(request):
    if request.method == "GET":
        students = Student.objects.all()
        student_data = [
            {
                "id": student.id,
                "name": student.name,
                "gender": student.gender,
                "date_of_birth": student.date_of_birth.strftime("%Y-%m-%d"),
                "major": student.major,
                "email": student.email,
                "contact_number": student.contact_number,
            }
            for student in students
        ]
        return JsonResponse({"students": student_data, "Response": True})


@csrf_exempt
def update_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )

    if request.method == "POST":
        data = json.loads(request.body)
        student.name = data["name"]
        student.gender = data["gender"]
        student.date_of_birth = data["date_of_birth"]
        student.major = data["major"]
        student.email = data["email"]
        student.contact_number = data["contact_number"]
        student.password = data["password"]  # Not recommended for real-world use
        student.save()
        return JsonResponse(
            {"message": "Student updated successfully", "response": True}
        )


@csrf_exempt
def delete_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        student.delete()
        return JsonResponse(
            {"message": "Student deleted successfully", "response": True}
        )


@csrf_exempt
def get_student_by_id(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        student_data = {
            "id": student.id,
            "name": student.name,
            "gender": student.gender,
            "date_of_birth": student.date_of_birth.strftime("%Y-%m-%d"),
            "major": student.major,
            "email": student.email,
            "contact_number": student.contact_number,
        }
        return JsonResponse({"student": student_data, "response": True})
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )
