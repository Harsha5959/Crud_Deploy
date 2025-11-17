from django.db import models

class employees(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    emp_email = models.EmailField()