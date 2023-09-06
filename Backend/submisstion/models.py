from django.db import models
from assignment.models import Assignment  # Import Assignment model
from students.models import Student  # Import Student model


class Submission(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField()
    STATUS_CHOICES = [
        ("Submitted", "Submitted"),
        ("Late", "Late"),
        ("Graded", "Graded"),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.student} - {self.assignment}"
