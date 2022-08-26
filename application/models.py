from distutils.command.upload import upload
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"
