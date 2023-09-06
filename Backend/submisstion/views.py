from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Student, Assignment, Submission
import json


# Add other imports if necessary
@csrf_exempt
def submit_assignment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        assignment_id = data.get("assignment_id")
        student_id = data.get("student_id")
        submission_date = data.get("submission_date")
        status = data.get("status")
        remarks = data.get("remarks")

        if (
            assignment_id is None
            or student_id is None
            or submission_date is None
            or status is None
        ):
            return JsonResponse(
                {
                    "message": "Assignment ID, Student ID, Submission Date, and Status are required",
                    "response": False,
                },
                status=400,
            )

        assignment = get_object_or_404(Assignment, id=assignment_id)
        student = get_object_or_404(Student, id=student_id)

        submission = Submission(
            assignment=assignment,
            student=student,
            submission_date=submission_date,
            status=status,
            remarks=remarks,
        )
        submission.save()

        return JsonResponse(
            {"message": "Assignment submitted successfully", "response": True}
        )


def get_submissions_for_assignment(request, assignment_id):
    try:
        assignment = Assignment.objects.get(id=assignment_id)
        submissions = Submission.objects.filter(assignment=assignment)

        submission_data = [
            {
                "id": submission.id,
                "student_id": submission.student_id,
                "submission_date": submission.submission_date.strftime("%Y-%m-%d"),
                "status": submission.status,
                "remarks": submission.remarks,
            }
            for submission in submissions
        ]

        return JsonResponse({"submissions": submission_data, "response": True})
    except Assignment.DoesNotExist:
        return JsonResponse(
            {"message": "Assignment not found", "response": False}, status=404
        )


def get_submissions_for_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        submissions = Submission.objects.filter(student=student)

        submission_data = [
            {
                "id": submission.id,
                "assignment_id": submission.assignment_id,
                "submission_date": submission.submission_date.strftime("%Y-%m-%d"),
                "status": submission.status,
                "remarks": submission.remarks,
            }
            for submission in submissions
        ]

        return JsonResponse({"submissions": submission_data, "response": True})
    except Student.DoesNotExist:
        return JsonResponse(
            {"message": "Student not found", "response": False}, status=404
        )
