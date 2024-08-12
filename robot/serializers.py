from rest_framework import serializers
from .models import Robot


# Robot serializer
class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = "__all__"
