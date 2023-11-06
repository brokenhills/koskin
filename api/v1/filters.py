from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from core.models import Writings


class DateWrRangeFilter(FilterSet):

    class Meta:
        model = Writings
        fields = ('datewr', )

    date = DateFromToRangeFilter(field_name='datewr')
