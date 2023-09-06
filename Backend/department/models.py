from django.db import models


class Department(models.Model):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    department_name = models.TextField()

    def __str__(self):
        return self.department_name
