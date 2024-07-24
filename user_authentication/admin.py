from django.contrib import admin
from .models import Signup, ContactUs, UserData

# Register your models here.
admin.site.register(Signup)
admin.site.register(ContactUs)
admin.site.register(UserData)