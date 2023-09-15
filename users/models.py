from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    parent_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subusers", null=True, blank=True
    )
    logo = models.ImageField(upload_to="media/logo/", blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    ntn = models.CharField(max_length=30, blank=True, null=True)
    strn = models.CharField(max_length=30, blank=True, null=True)
    registration_no = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    terms = models.TextField(null=True, blank=True)
    social_links = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "user_profile"
