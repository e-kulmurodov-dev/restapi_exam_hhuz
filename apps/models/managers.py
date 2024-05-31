from django.contrib.auth.models import UserManager


class AdminManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.ADMIN)


class EmployerManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(type=self.model.Type.EMPLOYER)
