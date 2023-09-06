from django.db import models
from course.models import Course  # Import Course model


class Assignment(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title
