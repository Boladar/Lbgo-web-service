from django.urls import path,include
from .import views

app_name = 'AdminPanel'

urlpatterns = [
    path('<str:eventName>/<str:objectiveCode>/',views.QRview, name='qr'),
    path('events/',views.EventListView.as_view(),name='events_list'),
    path('events/<str:pk>/',views.EventDetailView.as_view(),name='event_detail'),
    path('new/', views.EventCreateView.as_view(),name='event_create'),
]