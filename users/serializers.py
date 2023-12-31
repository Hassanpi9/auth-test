import random
import string
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["user"]
        extra_kwargs = {
            "active_key": {"read_only": True, "required": False},
            "active_flag": {"read_only": True, "required": False},
        }


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    def generate_unique_key(self):
        key = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(30)
        )
        return key

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        validated_data["password"] = make_password(validated_data["password"])
        unique_key = self.generate_unique_key()
        profile_data["active_key"] = unique_key
        user = super().create(validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.password = make_password(validated_data["password"])
            validated_data.pop("password")
        profile_data = validated_data.pop("profile", None)
        user = super().update(instance, validated_data)
        if profile_data:
            profile = user.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return user
