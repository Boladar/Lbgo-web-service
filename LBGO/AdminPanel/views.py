from django.shortcuts import render
from Database.models import Event,Objective
from django.views.generic import ListView, DetailView,CreateView,DeleteView

# Create your views here.

class EventCreateView(CreateView):
    template_name= 'AdminPanel/event_create.html'
    model = Event
    fields = ['name','startTime']

class EventDetailView(DetailView):
    template_name = 'AdminPanel/event_detail.html'
    model = Event

class EventListView(ListView):
    template_name = 'AdminPanel/event_list.html'
    model = Event

def QRview(request,eventName,objectiveCode):
    

    return render(request,'AdminPanel/qeTest.html',context={'eventName':eventName,'objectiveCode':objectiveCode})