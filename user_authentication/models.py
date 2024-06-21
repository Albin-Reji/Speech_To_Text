from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=150, primary_key=True)
    password = models.CharField(max_length=254)
    confirm_password = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.username} "

