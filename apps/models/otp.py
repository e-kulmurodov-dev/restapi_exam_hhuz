import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE, ForeignKey, CharField, DateTimeField
from django.utils import timezone

User = get_user_model()


class OTP(models.Model):
    user = ForeignKey('apps.User', CASCADE)
    otp = CharField(max_length=6)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.otp = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    def is_valid(self):
        return self.created_at > timezone.now() - timedelta(minutes=5)
