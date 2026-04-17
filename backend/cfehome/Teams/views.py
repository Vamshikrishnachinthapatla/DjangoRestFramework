from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from api.mixins import StaffEditorPermissionMixin
#UserQuerySetMixin
from .models import Team
from .serializers import TeamSerializer


class TeamListCreateAPIView(
   # UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
    ):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TeamRetrieveUpdateDestroyAPIView(
    #UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  
    
