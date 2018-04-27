from django.db import models

# Create your models here.
from student.models import Student


class Extend(models.Model):
    e_addr = models.CharField(max_length=50)
    e_tel = models.CharField(max_length=11)
    e_birth = models.DateField()
    e_des = models.CharField(max_length=50)
    s = models.OneToOneField(Student,null=True)
    class Meta:
        db_table = "extend"