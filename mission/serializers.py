from rest_framework import serializers
from robot.serializers import RobotSerializer
from .models import Mission


# Mission serializer
class MissionSerializer(serializers.ModelSerializer):
    """
    Mission Serializer for only Mission
    model fields.
    """

    class Meta:
        model = Mission
        fields = "__all__"


class MissionRetrieveSerializer(serializers.ModelSerializer):
    """
    Mission Serializer for Mission model
    fields and nested Robot model fields
    """

    robot = RobotSerializer()

    class Meta:
        model = Mission
        fields = "__all__"
