from django.shortcuts import render

from django.contrib.auth.models import User
from Database.models import Event, Objective
from Database.serializers import EventSerializer, ObjectiveSerializer

from rest_framework import viewsets
from rest_framework.generics import ListAPIView
# Create your views here.

class UserAllEventsAPIView(ListAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        queryset = Event.objects.all()

        username =  self.kwargs['username']
        if username is not None:
            queryset = queryset.filter(teams__members__username__exact = username)

        return queryset

class UserUpcomingEventsAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        username =  self.kwargs['username']
        if username is not None:
            queryset = queryset.filter(teams__members__username__exact = username)

        return queryset

class UserPastEventsAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        username =  self.kwargs['username']
        if username is not None:
            queryset = queryset.filter(teams__members__username__exact = username)

        return queryset

class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
