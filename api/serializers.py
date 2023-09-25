from rest_framework.serializers import ModelSerializer
from .models import datacon
from rest_framework import serializers



class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = datacon
        fields = '__all__'
