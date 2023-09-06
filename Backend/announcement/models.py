from django.db import models
from department.models import Department  # Import Department model
from course.models import Course  # Import Course model


class Announcement(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    title = models.TextField()
    description = models.TextField()
    publish_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
