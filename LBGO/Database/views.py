from django.shortcuts import render

from django.contrib.auth.models import User
from Database.models import Event
from Database.serializers import EventSerializer

from rest_framework import viewsets
# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
