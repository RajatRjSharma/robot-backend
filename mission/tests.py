from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mission.models import Mission
from robot.models import Robot


class MissionViewSetTests(APITestCase):
    """
    Test cases for Mission APIs.
    """

    def setUp(self):
        # Create a Robot instance
        self.robot = Robot.objects.create(
            name="Test Robot", model_name="Test Model Name", pose_x=100, pose_y=200
        )

        # Create a Mission instance
        self.mission = Mission.objects.create(
            name="Test Mission", description="Test Description", robot=self.robot
        )

        # Define URLs
        self.list_url = reverse("mission-list")
        self.detail_url = reverse("mission-detail", args=[self.mission.id])

    # Test GET list of missions
    def test_get_mission_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Test Mission")

    # Test GET single mission detail
    def test_get_mission_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Mission")

    # Test GET single mission detail not found
    def test_get_mission_detail_not_found(self):
        url = reverse("mission-detail", args=[9999])  # Non-existing ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Test POST valid data
    def test_create_mission(self):
        data = {
            "name": "New Mission",
            "description": "New Description",
            "robot": self.robot.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mission.objects.count(), 2)
        self.assertEqual(
            Mission.objects.get(id=response.data["id"]).name, "New Mission"
        )

    # Test POST invalid data
    def test_create_mission_invalid(self):
        data = {
            "name": "",  # Invalid name
            "description": "New Description",
            "robot": self.robot.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    # Test PUT valid data
    def test_update_mission(self):
        data = {
            "name": "Updated Mission",
            "description": "Updated Description",
            "robot": self.robot.id,
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.mission.refresh_from_db()
        self.assertEqual(self.mission.name, "Updated Mission")

    # Test PUT invalid data
    def test_update_mission_invalid(self):
        data = {
            "name": "",  # Invalid name
            "description": "Updated Description",
            "robot": self.robot.id,
        }
        response = self.client.put(self.detail_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)

    # Test DELETE valid data
    def test_delete_mission(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mission.objects.count(), 0)

    # Test DELETE on non-existing resource
    def test_delete_mission_not_found(self):
        url = reverse("mission-detail", args=[9999])  # Non-existing ID
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
