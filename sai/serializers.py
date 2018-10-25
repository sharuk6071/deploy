from rest_framework import serializers
from . models import ido

class idoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ido
        fields = '__all__'
