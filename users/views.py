from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserListCreateView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().select_related("profile")
        user_id = self.request.query_params.get("user_id")
        if user_id:
            queryset = queryset.filter(profile__parent_user_id=user_id)

        return queryset


class UserRetrieveUpdateDestroyView(generics.RetrieveAPIView):
    queryset = User.objects.all().select_related("profile")
    serializer_class = UserSerializer


class UpdateActiveFlagView(APIView):
    def post(self, request):
        username = request.data.get("username")
        active_key = request.data.get("active_key")

        try:
            user_profile = UserProfile.objects.get(user__username=username)
            if user_profile.active_key == active_key:
                user_profile.active_flag = True
                message = True
            else:
                user_profile.active_flag = False
                message = False
            user_profile.save()

            return Response(
                {"message": message},
                status=status.HTTP_200_OK,
            )
        except UserProfile.DoesNotExist:
            return Response(
                {"message": "User profile not found"}, status=status.HTTP_404_NOT_FOUND
            )
