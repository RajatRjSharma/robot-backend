from rest_framework import viewsets
from .models import Mission
from .serializers import MissionSerializer


# MissionViewSet GET-LIST GET-SINGLE POST PUT DELETE
class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
