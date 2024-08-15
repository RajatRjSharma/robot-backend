from rest_framework import serializers
from .models import Robot


# Robot serializer
class RobotSerializer(serializers.ModelSerializer):
    """
    Robot Serializer for all Robot fields.
    """

    class Meta:
        model = Robot
        fields = "__all__"
