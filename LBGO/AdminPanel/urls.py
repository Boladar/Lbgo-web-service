from django.urls import path,include
from .import views

app_name = 'AdminPanel'

urlpatterns = [
    path('<str:eventName>/<str:objectiveCode>/',views.QRview, name='qr'),
]