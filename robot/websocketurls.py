from django.urls import path
from robot.consumer import RobotMovementConsumer

# Web Socket url route
websocket_urlpatterns = [
    path("api/ws/movement/<int:robotID>/", RobotMovementConsumer.as_asgi()),
]
