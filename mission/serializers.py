from rest_framework import serializers
from .models import Mission


# Mission serializer
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = "__all__"
