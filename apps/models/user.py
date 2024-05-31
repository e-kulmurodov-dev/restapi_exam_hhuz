from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextChoices, BooleanField


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        EMPLOYER = 'Employer', 'Employer'

    type = CharField(max_length=255, choices=Type.choices, default=Type.EMPLOYER)
    # email_confirmed = BooleanField(default=False)
    # activation_link_used = BooleanField(default=False)

    class Meta:
        verbose_name = 'Employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return self.first_name
