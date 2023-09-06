from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Student
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password


@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Check if a student with the same email already exists
        existing_student = Student.objects.filter(email=data["email"]).first()

        if existing_student:
            # Student with the same email already exists
            return JsonResponse(
                {"message": "Student with this email already exists", "response": False}
            )

        # Hash the password before storing it
        hashed_password = make_password(data["password"])

        # Create and save the new student
        student = Student(
            name=data["name"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            major=data["major"],
            email=data["email"],
            password=hashed_password,  # Store the hashed password
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
        return JsonResponse({"students": student_data, "response": True})


@csrf_exempt
def update_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )

    if request.method == "PATCH":
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


@csrf_exempt
def student_login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            student = Student.objects.get(email=email)
            # Use check_password to verify the password
            if check_password(password, student.password):
                return JsonResponse(
                    {
                        "message": "Student login successful",
                        "response": True,
                        "user": {
                            "id": student.id,
                            "name": student.name,
                            "email": student.email,
                        },
                        "token": "StaticToken",
                    }
                )
            else:
                return JsonResponse(
                    {"message": "Wrong Credentials!!!", "response": False}
                )
        except Student.DoesNotExist:
            pass  # Student with the provided email doesn't exist or password doesn't match

    return JsonResponse(
        {"message": "Student login failed", "response": False}, status=401
    )
