from rest_framework import serializers
from sandbox.models import BuiltInFunction


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BuiltInFunction
        fields = ['name', 'description']
