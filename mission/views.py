from rest_framework import viewsets
from .models import Mission
from .serializers import MissionSerializer, MissionRetrieveSerializer


# MissionViewSet GET-LIST GET-SINGLE POST PUT DELETE
class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MissionRetrieveSerializer
        else:
            return MissionSerializer
