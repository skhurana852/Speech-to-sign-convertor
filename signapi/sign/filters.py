from django.contrib.auth.models import Sign
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Sign
        fields = ['title','description']