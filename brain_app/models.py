from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prediction_images/')
    date = models.DateField()
    result = models.CharField(max_length=255)

    def __str__(self):
        return self.result

