import django_filters
from .models import Comment


class CommentFilterSet(django_filters.FilterSet):
    # car = django_filters.NumberFilter(field_name='car__id')

    class Meta:
        model = Comment
        fields = (
            'car',
        )
