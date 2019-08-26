from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets          
from .serializers import SignSerializer      
from .models import Sign
from url_filter.integrations.drf import DjangoFilterBackend                     

class SignView(viewsets.ModelViewSet):       
    serializer_class = SignSerializer          
    queryset = Sign.objects.all()
    filter_backends=[DjangoFilterBackend]
    filter_fields=['description']
#added comment
