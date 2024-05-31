from django.db.models import CharField, TextField, ForeignKey, CASCADE, TextChoices, Model


class Vacancy(Model):
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    employer = ForeignKey('apps.user', CASCADE)

    class Type(TextChoices):
        FULL_TIME = 'full time', 'Full Time'
        PART_TIME = 'part time', 'Part Time'
        PROJECT_WORK = 'project work', 'Project Work'

    type = CharField(max_length=255, choices=Type.choices, default=Type.FULL_TIME)

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.title
