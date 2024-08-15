from django.db import models


# Robot model
class Robot(models.Model):
    """
    Robot model containing name, model_name,
    x and y coordinates.
    """

    name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    pose_x = models.FloatField()
    pose_y = models.FloatField()

    def __str__(self):
        return self.name
