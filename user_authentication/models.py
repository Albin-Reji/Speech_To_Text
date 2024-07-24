from django.core.validators import FileExtensionValidator
from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=150, primary_key=True)
    password = models.CharField(max_length=254)
    confirm_password = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.username} "
class UserData(models.Model):
    email = models.ForeignKey(Signup, on_delete=models.CASCADE)
    activity = models.FileField(upload_to='', validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'txt'])])
    def __str__(self):
        return f'{self.email.email} - {self.activity.name}'
class ContactUs(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=150, blank=False)
    message = models.TextField(max_length=280)

    def __str__(self):
        return  f"{self.name} {self.email}"