from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from robot.models import Robot


class RobotViewSetTests(APITestCase):
    """
    Testcases for Robot APIs.
    """

    def setUp(self):
        # Create a Robot instance
        self.robot = Robot.objects.create(
            name="Test Robot", model_name="Test Model Name", pose_x=100, pose_y=200
        )

        # Define URLs
        self.list_url = reverse("robot-list")
        self.detail_url = reverse("robot-detail", args=[self.robot.id])

    # Test GET list of robots
    def test_get_robot_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Robot")

    # Test GET single robot detail
    def test_get_robot_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Robot")

    # Test GET single robot detail not found
    def test_get_robot_detail_not_found(self):
        url = reverse("robot-detail", args=[9999])  # Non-existing ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test POST valid data
    def test_create_robot(self):
        data = {
            "name": "New Robot",
            "model_name": "Test New Model Name",
            "pose_x": 200,
            "pose_y": 300,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Robot.objects.count(), 2)
        self.assertEqual(Robot.objects.get(id=response.data["id"]).name, "New Robot")

    # Test POST invalid data
    def test_create_robot_invalid(self):
        data = {
            "name": "",  # Invalid name
            "model_name": "Test Model",
            "pose_x": "invalid",  # Invalid pose_x
            "pose_y": 200,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
        self.assertIn("pose_x", response.data)

    # Test PUT valid data
    def test_update_robot(self):
        data = {
            "name": "Updated Robot",
            "model_name": "Test Update Model Name",
            "pose_x": 150,
            "pose_y": 250,
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.robot.refresh_from_db()
        self.assertEqual(self.robot.name, "Updated Robot")

    # Test PUT invalid data
    def test_update_robot_invalid(self):
        data = {
            "name": "",  # Invalid name
            "model_name": "Test Update",
            "pose_x": "invalid",  # Invalid pose_x
            "pose_y": 50,
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
        self.assertIn("pose_x", response.data)

    # Test DELETE valid data
    def test_delete_robot(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Robot.objects.count(), 0)

    # Test DELETE on non-existing resource
    def test_delete_robot_not_found(self):
        url = reverse("robot-detail", args=[9999])  # Non-existing ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
