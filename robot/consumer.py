from channels.generic.websocket import JsonWebsocketConsumer
from django.core.serializers import serialize
import json


class RobotMovementConsumer(JsonWebsocketConsumer):

    def connect(self):
        from robot.models import Robot

        # Extract robotID from URL
        self.robot_id = self.scope["url_route"]["kwargs"]["robotID"]

        try:
            # Check if the Robot with the given ID exists
            self.robot = Robot.objects.get(id=self.robot_id)
            self.accept()  # Accept the WebSocket connection
            self.send_json(json.loads(serialize("json", [self.robot]))[0]["fields"])
        except Robot.DoesNotExist:
            self.close()  # Reject the connection if the Robot does not exist

    def disconnect(self, close_code):
        pass

    def receive_json(self, content):
        pose_x = content.get("pose_x")
        pose_y = content.get("pose_y")

        if isinstance(pose_x, (int, float)) and isinstance(
            pose_y, (int, float)
        ):  # Check if x and y coordinates are valid
            self.robot.pose_x = pose_x
            self.robot.pose_y = pose_y
            self.robot.save()  # Save the coordinates

            self.send_json({"status": True, "message": "coordinates_saved"})
        else:
            self.send_json({"status": False, "message": "invalid_data"})
