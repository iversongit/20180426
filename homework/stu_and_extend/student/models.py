from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_sex = models.BooleanField()
    s_age = models.IntegerField()
    s_school = models.CharField(max_length=20)
    s_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student"