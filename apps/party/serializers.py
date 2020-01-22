from rest_framework import serializers
from .models import Party

class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'