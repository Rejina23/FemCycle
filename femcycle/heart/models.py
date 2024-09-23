from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# myapp/models.py
class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField()
    length_of_cycle = models.IntegerField()
    length_of_menses = models.IntegerField(default=0)
    length_of_luteal = models.IntegerField()
    total_num_of_high_days = models.IntegerField()
    total_num_of_peak_days = models.IntegerField()
    total_days_of_fertility = models.IntegerField()
    total_fertility_formula = models.IntegerField(default=0)
    bmi = models.IntegerField(default=0)




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='')

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
