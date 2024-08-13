from django.urls import path
from robot.consumer import RobotMovementConsumer

websocket_urlpatterns = [
    path(
        "ws/movement/<int:robotID>/", RobotMovementConsumer.as_asgi()
    ),  # Define your WebSocket URL path
]
