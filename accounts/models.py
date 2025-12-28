from django.db import models
from django.contrib.auth.models import AbstractUser

class Advocate(AbstractUser):
    #django handles username, password, email, first name, last name automatically
    #Lets add the Advocate specific field to make advocate model
    phone_number = models.CharField(max_length = 15, blank = True, unique = True,error_messages = "Phone number already exists",  help_text = "Enter your phone number")
    license_number = models.CharField(max_length = 50, blank = True, unique = True, error_messages = "Liscense number already exists", help_text = "Enter your liscense number")
    specialization = models.CharField(max_length = 100, blank = True, help_text = "e.g., Criminal Law, Corporate Law, Family Law, etc.")


    #to check if admin has verified the user
    is_verified = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.username} - {self.email}"