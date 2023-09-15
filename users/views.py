from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().select_related("profile")
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(profile__parent_user_id=user_id)

        return queryset


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().select_related("profile")
    serializer_class = UserSerializer
