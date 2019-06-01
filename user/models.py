from django.db import models

# Create your models here.
class Details(models.Model):
    user_name = models.CharField(max_length=20)
    user_dob = models.DateField(auto_now_add=True)
    user_age = models.IntegerField()
    user_company = models.CharField(max_length=20)
    user_designation = models.CharField(max_length=20)
    user_phone = models.IntegerField()
    user_email = models.EmailField(null=True)
    user_working_hour = models.DurationField(null=True)
    user_resume = models.FileField(null=True, max_length=20)