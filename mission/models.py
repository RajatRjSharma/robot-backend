from django.db import models
from robot.models import Robot


# Mission model
class Mission(models.Model):
    """
    Model for Mission having name,
    description and robot.
    """

    name = models.CharField(max_length=100)
    description = models.TextField()
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
