from django.urls import path,include
from rest_framework import routers
from Database import views

app_name = 'Database'

router = routers.DefaultRouter()
router.register('events', views.EventViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]