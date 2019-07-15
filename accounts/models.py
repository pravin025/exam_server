import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class StudentProfile(models.Model):
    name = models.CharField(max_length=512)
    date_of_birth = models.DateField(null=True, blank=True)
    created_on = models.DateField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    phone = models.CharField(max_length=512)
    address = models.TextField()
    student_id = models.CharField(max_length=512)

    def __str__(self):
        return "{}_{}".format(self.user, self.name)


class ProfessorProfile(models.Model):
    name = models.CharField(max_length=512)
    created_on = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile')
    phone = models.CharField(max_length=512)
    address = models.TextField()
    professor_id = models.CharField(max_length=512)

    def __str__(self):
        return "{}/{}".format(self.user, self.name)


@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    profile_type = instance.profile_type
    now = datetime.datetime.now()
    if profile_type == 'professor':
        profile = ProfessorProfile.objects.get_or_create(user_id=instance.id)
        profile.professor_id = "exams@{}{}".format(instance.username, str(now.year))
    else:
        profile = StudentProfile.objects.get_or_create(user_id=instance.id)
        profile.student_id = "exams@{}{}".format(instance.username, str(now.year))
    profile.name = instance.name
    # profile.date_of_birth = instance[3]
    profile.phone = instance.phone
    profile.address = instance.address
