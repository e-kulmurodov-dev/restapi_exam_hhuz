from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.models import EmployerUserProxy, User, Vacancy


# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = 'id', 'first_name'
    filter_horizontal = ['groups', 'user_permissions']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.EMPLOYER
        obj.is_staff = True
        super().save_model(request, obj, form, change)


@admin.register(EmployerUserProxy)
class EmployerModelAdmin(BaseUserAdmin):

    def save_model(self, request, obj, form, change):
        obj.type = User.Type.EMPLOYER
        super().save_model(request, obj, form, change)


@admin.register(Vacancy)
class VacancyModelAdmin(admin.ModelAdmin):
    pass
