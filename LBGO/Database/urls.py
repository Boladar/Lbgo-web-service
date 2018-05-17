from django.urls import path,include
from rest_framework import routers
from Database import views

app_name = 'Database'

router = routers.DefaultRouter()
router.register('events', views.EventViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('<str:username>/events/past/',views.UserPastEventsAPIView.as_view()),
    path('<str:username>/events/upcoming/',views.UserUpcomingEventsAPIView.as_view()),
    path('<str:username>/events/all/',views.UserAllEventsAPIView.as_view()),
    path('objectives/<str:event_code>/<str:code>/',views.ObjectiveAPIView.as_view()),
]