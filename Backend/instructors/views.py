from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Instructor
import json


@csrf_exempt
def add_instructor(request):
    if request.method == "POST":
        data = json.loads(request.body)
        instructor = Instructor(
            name=data["name"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            department=data["department"],
            email=data["email"],
            contact_number=data["contact_number"],
            password=data["password"],
        )
        instructor.save()
        return JsonResponse(
            {"message": "Instructor added successfully", "response": True}
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

    if request.method == "POST":
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

    if request.method == "POST":
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
