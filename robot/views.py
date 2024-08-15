from rest_framework import viewsets
from .models import Robot
from .serializers import RobotSerializer


# RobotViewSet GET-LIST GET-SINGLE POST PUT DELETE
class RobotViewSet(viewsets.ModelViewSet):
    """
    Robot ViewSet accounting for all the APIs
    Such as GET(List/ID), POST, PUT, PATCH, DELETE
    """

    queryset = Robot.objects.all().order_by("id")
    serializer_class = RobotSerializer
