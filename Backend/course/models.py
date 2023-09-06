from django.db import models
from instructors.models import Instructor  # Import Instructor model


class Course(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    course_code = models.TextField()
    course_name = models.TextField()
    department = models.TextField()
    credits = models.PositiveIntegerField()
    description = models.TextField()
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE
    )  # Establish the relationship

    def __str__(self):
        return self.course_name
