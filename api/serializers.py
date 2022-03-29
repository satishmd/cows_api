from rest_framework import serializers
from .models import Cows

class CowsItemSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=100)
    collar_id = serializers.CharField(max_length=10)
    cow_number = serializers.CharField(max_length=30)
    collar_status = serializers.CharField(max_length=30)


    class Meta:
        model = Cows
        fields = ('__all__')