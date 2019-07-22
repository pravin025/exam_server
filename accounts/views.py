# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import UserSerializer
from django.contrib.auth.models import User


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

        _message = "success"
        status_code = status.HTTP_200_OK
        return Response(serializer.data, {"message": _message, "status_code": status_code})

    def retrieve(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk)
        user = User.objects.get(id=pk)
        user.delete()
        return Response({"data":"user Deleted Successfully"})

    

