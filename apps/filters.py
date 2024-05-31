from django_filters import FilterSet, CharFilter, ChoiceFilter

from apps.models import Vacancy


class VacancyFilter(FilterSet):
    type = ChoiceFilter(choices=Vacancy.Type.choices)
    title = CharFilter(field_name='title', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'type']

        # def filter_title(self, queryset, name, value):
        #     return queryset.filter(vacancy__title__icontains=value)
        #
        # def filter_description(self, queryset, name, value):
        #     return queryset.filter(vacancy__description__icontains=value)
