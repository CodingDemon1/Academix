from django.db import models
from students.models import Student  # Import Student model
from course.models import Course  # Import Course model
from django.utils import timezone


class Enrollment(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.student} - {self.course}"
