from django.urls import path, include
from . import views

app_name = "students"

urlpatterns = [
    path("add/", views.add_student, name="add_student"),
    path("", views.get_students, name="get_students"),
    path("update/<int:student_id>/", views.update_student, name="update_student"),
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
    path("login/", views.student_login_view, name="student-login"),
    path("<str:student_id>/", views.get_student_by_id, name="get_student_by_id"),
]
