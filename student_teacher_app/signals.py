from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.urls import reverse
from .views import verify


@receiver(signals.post_save,sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if not instance.is_staff:
        print("inside email")
        # Send verification email
        send_mail(
            'Verify your celery account',
            'Follow this link to verify your account: '
            'http://127.0.0.1:8000/stu%s' % reverse('views.verify'),
            'pooja115239@gmail.com',
            [instance.email],
            fail_silently=False,
        )
    print("email sent")