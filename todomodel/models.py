from django.db import models

# Create your models here.
class Userdata (models.Model):
    user_input = models.CharField(max_length=50)