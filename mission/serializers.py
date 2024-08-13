from rest_framework import serializers
from robot.serializers import RobotSerializer
from .models import Mission


# Mission serializer
class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = "__all__"


class MissionRetrieveSerializer(serializers.ModelSerializer):
    robot = RobotSerializer()

    class Meta:
        model = Mission
        fields = "__all__"
