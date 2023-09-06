from django.shortcuts import render
from .models import Department
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json


# Create your views here.
@csrf_exempt
def create_department(request):
    if request.method == "POST":
        data = json.loads(request.body)
        department_name = data.get("department_name")

        if department_name is None:
            return JsonResponse(
                {"message": "Department name is required", "response": False},
                status=400,
            )

        department = Department(department_name=department_name)
        department.save()

        return JsonResponse(
            {"message": "Department created successfully", "response": True}
        )


@csrf_exempt
def update_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == "PATCH":
        data = json.loads(request.body)
        department_name = data.get("department_name")

        if department_name is not None:
            department.department_name = department_name
            department.save()
            return JsonResponse(
                {"message": "Department updated successfully", "response": True}
            )
        else:
            return JsonResponse(
                {"message": "Department name is required", "response": False},
                status=400,
            )


@csrf_exempt
def delete_department(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return JsonResponse(
            {"message": "Department not found", "response": False}, status=404
        )

    if request.method == "DELETE":
        department.delete()
        return JsonResponse(
            {"message": "Department deleted successfully", "response": True}
        )


def get_department_by_id(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
        department_data = {
            "id": department.id,
            "department_name": department.department_name,
        }
        return JsonResponse({"department": department_data, "response": True})
    except Department.DoesNotExist:
        return JsonResponse(
            {"message": "Department not found", "response": False}, status=404
        )


def get_all_departments(request):
    departments = Department.objects.all()

    department_data = [
        {
            "id": department.id,
            "department_name": department.department_name,
        }
        for department in departments
    ]

    return JsonResponse({"departments": department_data, "response": True})
