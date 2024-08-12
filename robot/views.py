from rest_framework import viewsets
from .models import Robot
from .serializers import RobotSerializer


# RobotViewSet GET-LIST GET-SINGLE POST PUT DELETE
class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
