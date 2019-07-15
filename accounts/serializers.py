from rest_framework import serializers
from django.contrib.auth.models import User

from .models import StudentProfile, ProfessorProfile


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('name', 'date_of_birth', 'created_on', 'user', 'phone', 'address', 'student_id')


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorProfile
        fields = ('name', 'created_on', 'user', 'phone', 'address', 'professor_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name')
