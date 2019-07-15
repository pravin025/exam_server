from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ProfessorProfile, StudentProfile, UserSerializer
from django.contrib.auth.models import User

from .models import StudentProfile, ProfessorProfile


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def list(self, request):
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        payload = request.data
        user_payload = {
            "username": payload.get("username"),
            "password": payload.get("password"),
            "email": payload.get("email")
        }
        serializer = UserSerializer(user_payload)
        user = User.objects.create_user(serializer.data)
        user.name = payload.get("name")
        user.profile_type = payload.get("prafile_type")
        user.phone = payload.get("phone")
        user.address = payload.get("address")
        user.save()

        return Response(serializer.data)
