from rest_framework import serializers
from .models import Team

class TeamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Team
        fields = ['id','owner','name','sponsor','country','division','trophies']


