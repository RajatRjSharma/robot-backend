from rest_framework import viewsets
from .models import Mission
from .serializers import MissionSerializer, MissionRetrieveSerializer


# MissionViewSet GET-LIST GET-SINGLE POST PUT DELETE
class MissionViewSet(viewsets.ModelViewSet):
    """
    Mission ViewSet accounting for all the APIs
    Such as GET(List/ID), POST, PUT, PATCH, DELETE
    """

    queryset = Mission.objects.all().order_by("id")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MissionRetrieveSerializer
        else:
            return MissionSerializer
