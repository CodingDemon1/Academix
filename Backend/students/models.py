from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    name = models.TextField()
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    major = models.TextField()
    email = models.EmailField()
    contact_number = models.TextField()
    password = models.CharField(max_length=128)  # Not recommended for real-world use

    def __str__(self):
        return self.name
