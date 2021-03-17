from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.core.mail import send_mail
from django.urls import reverse


class UserRoleMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1)  # S for student and T for teacher

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name