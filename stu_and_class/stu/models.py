from django.db import models

# Create your models here.
from classroom.models import Grade


class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_operate_time = models.DateTimeField(auto_now=True)
    g = models.ForeignKey(Grade)

    class Meta:
        db_table = "tb_student"