from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mac_address = models.CharField(max_length=50)
    active_flag = models.BooleanField(default=False)
    active_key = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = "user_profile"
