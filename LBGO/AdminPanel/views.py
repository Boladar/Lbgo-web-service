from django.shortcuts import render
from Database.models import Event

# Create your views here.

def QRview(request,eventName,objectiveCode):
    

    return render(request,'AdminPanel/qeTest.html',context=None)