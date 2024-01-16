import django_filters
from .models import Ad


class AdTitleFilter(django_filters.FilterSet):
    """
    Custom Filter for searching coincidence in Ad title.
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains", )

    class Meta:
        model = Ad
        fields = ("title",)
