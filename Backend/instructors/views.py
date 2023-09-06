from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Instructor
import json
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.hashers import make_password, check_password


@csrf_exempt
def add_instructor(request):
    if request.method == "POST":
        data = json.loads(request.body)

        existing_instructor = Instructor.objects.filter(email=data["email"])

        if existing_instructor:
            return JsonResponse(
                {
                    "message": "Instructor with this email already exists",
                    "response": False,
                }
            )
        instructor = Instructor(
            name=data["name"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            department=data["department"],
            email=data["email"],
            contact_number=data["contact_number"],
            password=make_password(data["password"]),
        )
        instructor.save()
        return JsonResponse(
            {"message": "Instructor Registered successfully", "response": True}
        )


@csrf_exempt
def get_instructors(request):
    if request.method == "GET":
        instructors = Instructor.objects.all()
        instructor_data = [
            {
                "id": instructor.id,
                "name": instructor.name,
                "gender": instructor.gender,
                "date_of_birth": instructor.date_of_birth.strftime("%Y-%m-%d"),
                "department": instructor.department,
                "email": instructor.email,
                "contact_number": instructor.contact_number,
                "isAuthorized": instructor.isAuthorized,
            }
            for instructor in instructors
        ]
        return JsonResponse({"instructors": instructor_data, "response": True})


@csrf_exempt
def update_instructor(request, instructor_id):
    try:
        instructor = Instructor.objects.get(id=instructor_id)
    except Instructor.DoesNotExist:
        return JsonResponse(
            {"message": "Instructor not found", "response": False}, status=404
        )

    if request.method == "PATCH":
        data = request.POST
        instructor.name = data["name"]
        instructor.gender = data["gender"]
        instructor.date_of_birth = data["date_of_birth"]
        instructor.department = data["department"]
        instructor.email = data["email"]
        instructor.contact_number = data["contact_number"]
        instructor.save()
        return JsonResponse(
            {"message": "Instructor updated successfully", "response": True}
        )


@csrf_exempt
def delete_instructor(request, instructor_id):
    try:
        instructor = Instructor.objects.get(id=instructor_id)
    except Instructor.DoesNotExist:
        return JsonResponse(
            {"message": "Instructor not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        instructor.delete()
        return JsonResponse(
            {"message": "Instructor deleted successfully", "response": True}
        )


@csrf_exempt
def get_instructor_by_id(request, instructor_id):
    try:
        instructor = Instructor.objects.get(id=instructor_id)
        instructor_data = {
            "id": instructor.id,
            "name": instructor.name,
            "gender": instructor.gender,
            "date_of_birth": instructor.date_of_birth.strftime("%Y-%m-%d"),
            "department": instructor.department,
            "email": instructor.email,
            "contact_number": instructor.contact_number,
        }
        return JsonResponse({"instructor": instructor_data, "response": True})
    except Instructor.DoesNotExist:
        return JsonResponse(
            {"message": "Instructor not found", "response": False}, status=404
        )


@csrf_exempt
def instructor_login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        try:
            instructor = Instructor.objects.get(email=email)
            if check_password(password, instructor.password):
                return JsonResponse(
                    {
                        "message": "Instructor login successful",
                        "response": True,
                        "user": {
                            "id": instructor.id,
                            "name": instructor.name,
                            "email": instructor.email,
                            "department": instructor.department,
                        },
                        "token": "StaticToken",
                    }
                )
            else:
                JsonResponse({"message": "Wrong Credentials!!!", "response": False})
        except Instructor.DoesNotExist:
            pass  # Instructor with the provided email doesn't exist or password doesn't match

    return JsonResponse(
        {"message": "Instructor login failed", "response": False}, status=401
    )
