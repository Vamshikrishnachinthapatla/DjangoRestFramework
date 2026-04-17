from django.urls import path
from .views import (
    TeamListCreateAPIView,
    TeamRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('teams/', TeamListCreateAPIView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamRetrieveUpdateDestroyAPIView.as_view(), name='team-detail')
]
