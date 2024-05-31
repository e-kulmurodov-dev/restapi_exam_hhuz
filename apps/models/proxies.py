from apps.models.managers import AdminManager, EmployerManager
from apps.models import User


class AdminUserProxy(User):
    objects = AdminManager()

    class Meta:
        proxy = True
        verbose_name = "Admin"
        verbose_name_plural = "Admins"


class EmployerUserProxy(User):
    objects = EmployerManager()

    class Meta:
        proxy = True
        verbose_name = "Employer"
        verbose_name_plural = "Employers"
