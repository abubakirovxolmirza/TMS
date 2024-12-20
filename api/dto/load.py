from rest_framework import serializers
from apps.load.models import Load

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = '__all__'
